// Получаем элементы кнопок и списков
const byDateButton = document.getElementById('byDateButton');
const bySubjectButton = document.getElementById('bySubjectButton');
const byDateList = document.getElementById('byDateList');
const bySubjectList = document.getElementById('bySubjectList');

// Функция для переключения видимости списков
function switchList(buttonClicked, listToShow, listToHide) {
    // Показываем нужный список
    listToShow.style.display = 'block';
    // Скрываем другой список
    listToHide.style.display = 'none';

    // Убираем активный класс с обеих кнопок
    byDateButton.classList.remove('active');
    bySubjectButton.classList.remove('active');

    // Добавляем активный класс к кнопке, которая была нажата
    buttonClicked.classList.add('active');
}

// Добавляем обработчики событий для кнопок
byDateButton.addEventListener('click', function() {
    switchList(byDateButton, byDateList, bySubjectList);
});

bySubjectButton.addEventListener('click', function() {
    switchList(bySubjectButton, bySubjectList, byDateList);
});

// Изначально показываем список по дате
switchList(byDateButton, byDateList, bySubjectList);


