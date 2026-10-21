// This function runs inside the selected element's frame. Keep it self-contained.
export function selectorForElement(element) {
  const document = element.ownerDocument;
  const tag = element.tagName.toLowerCase();
  for (const name of ['id', 'data-testid', 'data-test', 'name', 'aria-label', 'placeholder']) {
    const value = element.getAttribute(name);
    if (!value) continue;
    const selector = `${tag}[${name}=${JSON.stringify(value)}]`;
    const matches = document.querySelectorAll(selector);
    if (matches.length === 1 && matches[0] === element) return selector;
  }
  const parts = [];
  for (let current = element; current; current = current.parentElement) {
    let part = current.tagName.toLowerCase();
    if (current.parentElement) {
      const siblings = [...current.parentElement.children].filter((node) => node.tagName === current.tagName);
      if (siblings.length > 1) part += `:nth-of-type(${siblings.indexOf(current) + 1})`;
    }
    parts.unshift(part);
    const selector = parts.join(' > ');
    const matches = document.querySelectorAll(selector);
    if (matches.length === 1 && matches[0] === element) return selector;
  }
  throw new Error('无法为所选元素生成唯一选择器');
}

async function frameSpec(page, frame, element) {
  const selector = await element.evaluate(selectorForElement);
  if (frame === page.mainFrame()) return selector;
  if (frame.parentFrame() !== page.mainFrame()) throw new Error('暂不支持多层嵌套 iframe，请使用手工配置');
  const iframe = await frame.frameElement();
  try { return { selector, frame: await iframe.evaluate(selectorForElement) }; }
  finally { await iframe.dispose(); }
}

export async function pickField(page, kind, label) {
  const name = `__novel_picker_${Date.now()}_${Math.random().toString(36).slice(2)}`;
  const installed = [];
  let timer;
  let closeListener;
  let settled = false;
  let rejectSelection;
  let resolveSelection;
  let binding;
  const selection = new Promise((resolve, reject) => {
    resolveSelection = resolve;
    rejectSelection = reject;
    timer = setTimeout(() => reject(new Error(`点选 ${label} 超时，请重新运行 setup`)), 300000);
    closeListener = () => reject(new Error('校准期间浏览器页面已关闭'));
    page.once('close', closeListener);
  });
  // Catch immediately: a page can close while listeners are still being installed.
  selection.catch(() => {});
  try {
    binding = await page.exposeBinding(name, async ({ frame }, selected) => {
      if (settled) return;
      settled = true;
      let handle;
      try {
        if (selected !== true) throw new Error('已取消点选');
        // Modern Playwright bindings pass serializable arguments, not DOM handles.
        handle = await frame.evaluateHandle((binding) => window[binding + '_selected'], name);
        if (!await handle.evaluate((element) => Boolean(element && element.nodeType === 1))) throw new Error('所选元素已失效');
        resolveSelection(await frameSpec(page, frame, handle));
      } catch (error) { rejectSelection(error); }
      finally { await handle?.dispose(); }
    });
    for (const frame of page.frames()) {
      try {
        await frame.evaluate(({ name, kind, label }) => {
          if (!document.documentElement) return;
          const banner = document.createElement('div');
          banner.textContent = `小说发布助手：请点选${label}（本次点击仅用于识别，不会执行原按钮；Esc 取消）`;
          banner.style.cssText = 'position:fixed;top:0;left:0;right:0;z-index:2147483647;background:#172554;color:white;padding:12px;font:14px sans-serif;pointer-events:none;';
          document.documentElement.append(banner);
          const events = ['pointerdown', 'pointerup', 'mousedown', 'mouseup', 'click', 'dblclick', 'submit'];
          const block = (event) => {
            event.preventDefault();
            event.stopImmediatePropagation();
            if (event.type !== 'click') return;
            const target = event.target instanceof Element ? event.target : event.target?.parentElement;
            const editable = kind === 'title'
              ? 'input:not([type]), input[type="text"], textarea, [contenteditable="true"], [contenteditable="plaintext-only"]'
              : 'textarea, [contenteditable="true"], [contenteditable="plaintext-only"]';
            const element = target?.closest(kind === 'button' ? 'button, [role="button"], input[type="button"], input[type="submit"], a' : editable);
            if (element) {
              window[name + '_selected'] = element;
              void window[name](true);
            }
          };
          const key = (event) => {
            event.preventDefault();
            event.stopImmediatePropagation();
            if (event.key === 'Escape') void window[name](null);
          };
          for (const event of events) document.addEventListener(event, block, true);
          document.addEventListener('keydown', key, true);
          window[name + '_cleanup'] = () => {
            for (const event of events) document.removeEventListener(event, block, true);
            document.removeEventListener('keydown', key, true);
            banner.remove();
            delete window[name + '_selected'];
            delete window[name + '_cleanup'];
          };
        }, { name, kind, label });
        installed.push(frame);
      } catch (error) {
        // Never leave an unprotected embedded frame where selecting a button could submit.
        rejectSelection(new Error(`无法安全启用字段点选：${error.message}`));
        throw error;
      }
    }
    console.log(`请在浏览器中点选：${label}（只捕获元素，不执行原按钮）`);
    return await selection;
  } finally {
    settled = true;
    clearTimeout(timer);
    page.off('close', closeListener);
    await Promise.all(installed.map((frame) => frame.evaluate((binding) => {
      window[binding + '_cleanup']?.();
    }, name).catch(() => {})));
    await binding?.dispose();
  }
}

export async function calibratePage(page, config, { includePublish = false } = {}) {
  const origin = new URL(config.editorUrl).origin;
  if (new URL(page.url()).origin !== origin) throw new Error('请进入七猫作者后台的编辑页面后再校准，当前页面不属于配置站点');
  const title = await pickField(page, 'title', '小说标题输入框');
  const body = await pickField(page, 'body', '小说正文编辑框');
  if (JSON.stringify(title) === JSON.stringify(body)) throw new Error('标题和正文选中了同一个元素，请重新校准');
  const save = await pickField(page, 'button', '保存草稿按钮');
  const actions = { save: { button: save, success: { manual: true } } };
  if (includePublish) {
    actions.publish = { button: await pickField(page, 'button', '发布按钮'), success: { manual: true } };
  }
  if (new URL(page.url()).origin !== origin) throw new Error('校准期间页面站点改变，未保存配置');
  return {
    ...config, configured: true, editorUrl: page.url(), manualNewEntry: true,
    fields: { title, body }, actions,
  };
}
