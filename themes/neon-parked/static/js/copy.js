document.addEventListener('DOMContentLoaded', () => {
  const copyIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
  const checkIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';

  document.querySelectorAll('.page-content pre').forEach(block => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.innerHTML = `${copyIcon} <span>COPY</span>`;

    button.addEventListener('click', async () => {
      const code = block.querySelector('code').innerText;
      try {
        await navigator.clipboard.writeText(code);
        button.innerHTML = `${checkIcon} <span>COPIED</span>`;
        button.classList.add('copied');
        setTimeout(() => {
          button.innerHTML = `${copyIcon} <span>COPY</span>`;
          button.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Failed to copy: ', err);
      }
    });

    block.appendChild(button);
  });
});
