document.addEventListener('DOMContentLoaded', () => {
    const themeButtons = {
        standart: document.getElementById('theme-standart'),
        light: document.getElementById('theme-light'),
        dark: document.getElementById('theme-dark'),
    };

    const elements = [
        { selector: 'body', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'button', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'h1', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'h2', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'header', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'a.settings-link', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'a', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'a.arrow-right', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: 'a.arrow-left', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.day li', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.schedule_all ul', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.schedule-time li', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.ocn', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-border', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-select', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-select.active', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-select', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-button', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.login-body', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.rasp li', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        { selector: '.homework', classes: ['standart-theme', 'light-theme', 'dark-theme'] },



    ];

    // Проверяем сохраненную тему в localStorage
    const savedTheme = localStorage.getItem('theme') || 'standart-theme';
    applyTheme(savedTheme);

    // Привязываем обработчики событий к кнопкам
    Object.keys(themeButtons).forEach(theme => {
        themeButtons[theme].addEventListener('click', () => {
            applyTheme(`${theme}-theme`);
            localStorage.setItem('theme', `${theme}-theme`); // Сохраняем выбор темы
        });
    });

    function applyTheme(theme) {
        elements.forEach(({ selector, classes }) => {
            document.querySelectorAll(selector).forEach(element => {
                classes.forEach(cls => element.classList.remove(cls));
                element.classList.add(theme);
            });
        });
    }
});

