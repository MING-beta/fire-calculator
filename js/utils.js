// js/utils.js

export const formatCurrency = (amountInTenK) => {
    if (amountInTenK < 0) return '0';

    const eok = Math.floor(amountInTenK / 10000);
    const man = Math.floor(amountInTenK % 10000);

    if (eok > 0) {
        return man > 0 ? `${eok.toLocaleString()}억 ${man.toLocaleString()}만` : `${eok.toLocaleString()}억`;
    }
    return `${man.toLocaleString()}만`;
};

export const parseFormattedNumber = (val) => {
    if (!val) return 0;
    return parseFloat(String(val).replace(/,/g, '')) || 0;
};

export const trackEvent = (action, category, label, value) => {
    const gtagFunc = window.gtag || window.parent?.gtag;
    if (typeof gtagFunc === 'function') {
        gtagFunc('event', action, {
            'event_category': category,
            'event_label': label,
            'value': value,
            'send_to': 'G-YWC7FQQ34S'
        });
    }
    console.log(`[Analytics] ${category} > ${action}: ${label}`);
};

export const showToast = (message, duration = 3000) => {
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.style.cssText = `
            position: fixed;
            bottom: 24px;
            left: 24px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 10000;
            pointer-events: none;
        `;
        document.body.appendChild(toastContainer);
    }

    const toast = document.createElement('div');
    toast.className = 'fade-in-up';
    toast.style.cssText = `
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(168, 85, 247, 0.4);
        border-left: 4px solid var(--text-accent);
        color: #fff;
        padding: 12px 16px;
        border-radius: 8px;
        font-size: 14px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        backdrop-filter: blur(8px);
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s ease;
        pointer-events: auto;
    `;

    toast.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--text-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        <span>${message}</span>
    `;

    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => {
            if (toast.parentElement) toast.remove();
        }, 300);
    }, duration);
};

export const showModalDialog = (htmlContent, callback) => {
    const overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    overlay.style.zIndex = '2000';
    overlay.innerHTML = `
        <div class="modal-content glassmorphism" style="max-width:320px; text-align:center;">
            ${htmlContent}
        </div>
    `;
    document.body.appendChild(overlay);

    const closeBtn = overlay.querySelector('.close-dialog') || overlay.querySelector('.cancel-dialog');
    const confirmBtn = overlay.querySelector('.confirm-dialog');
    const input = overlay.querySelector('input');

    if (input) input.focus();

    const close = (value) => {
        overlay.classList.add('hidden');
        setTimeout(() => overlay.remove(), 300);
        callback(value);
    };

    if (closeBtn) closeBtn.addEventListener('click', () => close(null));
    if (confirmBtn) confirmBtn.addEventListener('click', () => close(input ? input.value : true));

    if (input) {
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') close(input.value);
        });
    }
};

export const customPrompt = (message, defaultValue) => {
    return new Promise(resolve => {
        showModalDialog(`
            <h3 style="font-size:16px; margin-bottom:16px; color:#fff;">새 프로필 저장</h3>
            <p style="font-size:14px; color:var(--text-secondary); margin-bottom:12px;">${message}</p>
            <input type="text" value="${defaultValue || ''}" style="width:100%; padding:10px; border-radius:8px; border:1px solid var(--border-glass); background:var(--bg-input); color:#fff; margin-bottom:16px; outline:none;" />
            <div style="display:flex; gap:8px;">
                <button class="cancel-dialog" style="flex:1; padding:10px; border-radius:8px; border:1px solid var(--border-glass); background:transparent; color:#fff; cursor:pointer;">취소</button>
                <button class="confirm-dialog" style="flex:1; padding:10px; border-radius:8px; border:none; background:var(--accent-gradient); color:#fff; cursor:pointer; font-weight:600;">확인</button>
            </div>
        `, resolve);
    });
};

export const customConfirm = (message) => {
    return new Promise(resolve => {
        showModalDialog(`
            <h3 style="font-size:16px; margin-bottom:16px; color:#fff;">확인</h3>
            <p style="font-size:14px; color:var(--text-secondary); margin-bottom:20px;">${message}</p>
            <div style="display:flex; gap:8px;">
                <button class="cancel-dialog" style="flex:1; padding:10px; border-radius:8px; border:1px solid var(--border-glass); background:transparent; color:#fff; cursor:pointer;">취소</button>
                <button class="confirm-dialog" style="flex:1; padding:10px; border-radius:8px; border:none; background:var(--accent-gradient); color:#fff; cursor:pointer; font-weight:600;">확인</button>
            </div>
        `, resolve);
    });
};
