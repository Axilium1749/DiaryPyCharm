document.addEventListener('DOMContentLoaded', () => {
    // Кнопки для переключения тем
    const themeButtons = {
        standart: document.getElementById('theme-standart'),
        light: document.getElementById('theme-light'),
        dark: document.getElementById('theme-dark'),
    };

    // Логотипы (элементы img)
    const logoElements = [
        { id: 'hw-logo', standardSrc: '..\\img\\logo\\hw-logo-standart.svg', lightSrc: '..\\img\\logo\\hw-logo-light.svg', darkSrc: '..\\img\\logo\\hw-logo-dark.svg' },
        { id: 'logo-login', standardSrc: '..\\img\\logo\\hw-logo-standart.svg', lightSrc: '..\\img\\logo\\hw-logo-light.svg', darkSrc: '..\\img\\logo\\hw-logo-dark.svg' },
        { id: 'beha-logo', standardSrc: '..\\img\\logo\\beha-logo-standart.svg', lightSrc: '..\\img\\logo\\beha-logo-light.svg', darkSrc: '..\\img\\logo\\beha-logo-dark.svg' },
        { id: 'sett-logo', standardSrc: '..\\img\\logo\\marks-logo-standart.svg', lightSrc: '..\\img\\logo\\marks-logo-light.svg', darkSrc: '..\\img\\logo\\marks-logo-dark.svg' },
        { id: 'marks-logo', standardSrc: '..\\img\\logo\\marks-logo-standart.svg', lightSrc: '..\\img\\logo\\marks-logo-light.svg', darkSrc: '..\\img\\logo\\marks-logo-dark.svg' },
        { id: 'notif-logo', standardSrc: '..\\img\\logo\\notif-logo-standart.svg', lightSrc: '..\\img\\logo\\notif-logo-light.svg', darkSrc: '..\\img\\logo\\notif-logo-dark.svg' },
        { id: 'sett-icon', standardSrc: '..\\img\\settings.svg', lightSrc: '..\\img\\settings.svg', darkSrc: '..\\img\\settings-dark-theme.svg' },

    ];

    // Проверяем сохраненную тему в localStorage
    const savedTheme = localStorage.getItem('theme') || 'standart-theme';
    applyTheme(savedTheme);

    // Привязываем обработчики событий к кнопкам для смены темы
    Object.keys(themeButtons).forEach(theme => {
        themeButtons[theme].addEventListener('click', () => {
            applyTheme(`${theme}-theme`);
            localStorage.setItem('theme', `${theme}-theme`); // Сохраняем выбор темы
        });
    });

    // Функция для применения выбранной темы
    function applyTheme(theme) {
        // Применяем классы для элементов (например, body, заголовки, кнопки)
        const elements = [
            { selector: 'body', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
            { selector: 'button', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
            { selector: 'h1', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
            { selector: 'h2', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
            { selector: 'header', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
            { selector: 'a.settings-link', classes: ['standart-theme', 'light-theme', 'dark-theme'] },
        ];

        elements.forEach(({ selector, classes }) => {
            document.querySelectorAll(selector).forEach(element => {
                classes.forEach(cls => element.classList.remove(cls));
                element.classList.add(theme);
            });
        });

        // Применяем тему для логотипов
        logoElements.forEach(({ id, standardSrc, lightSrc, darkSrc }) => {
            const imgElement = document.getElementById(id);
            if (imgElement) {
                switch (theme) {
                    case 'standart-theme':
                        imgElement.src = standardSrc;
                        break;
                    case 'light-theme':
                        imgElement.src = lightSrc;
                        break;
                    case 'dark-theme':
                        imgElement.src = darkSrc;
                        break;
                }
            }
        });
    }
});
