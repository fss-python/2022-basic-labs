# Лабораторные работы для 1-го курса магистратуры ФСН (2021/2022)

В рамках факультатива "Программирование для психофизиологов" в ННГУ им. Н. И. Лобачевского.

Курс направлен на освоение языка программирования Python для решения стандартных 
задач психофизиолога по анализу сигналов и данных.

В данном курсе формируются базовые знания для последующего освоения:

- основных библиотек для анализа EEG, ECG, eye-tracking и пр.;
- библиотек для статистического анализа данных;
- библиотек для конструирования психофизиологических экспериментов.

Преподаватели: 

* [Демидовский Александр Владимирович](https://www.hse.ru/staff/demidovs) - лектор
* [Бахчина Анастасия Владимировна](https://ipran.ru/profile/%D0%B1%D0%B0%D1%85%D1%87%D0%B8%D0%BD%D0%B0-%D0%B0%D0%BD%D0%B0%D1%81%D1%82%D0%B0%D1%81%D0%B8%D1%8F-%D0%B2%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%BD%D0%B0/) - консультант
* [Чихачёв Алексей Владимирович](https://t.me/alexeyc7) - ментор

План лабораторных работ:

1. [Детектирование RR-интервалов в кардиограмме человека](./lab_1/lab_1.md)
   1. Дедлайн: 22 марта
1. [Расчет диагностических показателей временной области для последовательностей RR-интервалов](./lab_2/lab_2.md)
   1. Дедлайн: 26 апреля
1. [Статистическое сравнение состояния участников по показателям RR-интервалов между разными тестами эксперимента](./lab_3/lab_3.md)
   1. Дедлайн: 17 мая

## Ресурсы

1. [Таблица успеваемости](https://docs.google.com/spreadsheets/d/19R8gMTneL54dk5Ou_GqeiSuQwW_HrANvg8oKZOtd1fc/edit?usp=sharing)
1. Используемые данные. Источник: 
   [POPANE DATASET - Psychophysiology Of Positive And Negative Emotions](https://osf.io/94bpx/).
   В результате выполнения лабораторных работ будут использоваться некоторое подмножество
   этих данных. Об их структуре, а также о структуре получаемых артефактов, подробнее
   в [отдельном документе](./docs/data/md).

## История занятий

|Дата|Тема лекции|Запись занятия|Листинги кода|
|:--:|:---|:---|:---|
|15.02.2022|Знакомство. Историческая справка. Преимущества и недостатки языка Python.|[Видео урока](https://drive.google.com/file/d/15qGMMg1gm2LPKEMhU_dYj6rXufUlqGt9/view?usp=sharing)|N/A|
|22.02.2022|Выполнение программ на Python. Работа с числами. Разбираемся с заданием лабораторной работы|[Видео урока](https://drive.google.com/file/d/13lmOBSIps2vlYVWsYLR7Poo1HH4LJEwQ/view?usp=sharing)|[Листинг](./seminars/02.22.2022/practice_2.py)|
|02.03.2022|Работа со списками: создание, изменение, основные свойства. Цикл `for`: базовый синтаксис, `break`  и  `continue`.|[Видео урока](https://drive.google.com/file/d/1TwIsu6NB_5TnHYsTALhOjkLfamwWG9Aj/view?usp=sharing)|[Листинг](./seminars/03.02.2022/practice_3.py)|
|09.03.2022|Функции: знакомство и базовый синтаксис.|[Видео урока](https://drive.google.com/file/d/170wSmMz84cWt_iZgS6taz3P0tRVgE7gN/view?usp=sharing)|[Листинг](./seminars/03.09.2022/practice_4.py)|
|15.03.2022|Функции: формулируем алгоритм и выражаем средствами языка. Строки - неизменяемые последовательности, методы `join` и `split`.|[Видео урока](https://drive.google.com/file/d/1cowRg6FCzn5RUNWOvt1XoZf0uXnIZqhW/view?usp=sharing)|[Листинг](./seminars/03.15.2022/practice_5.py)|
|22.03.2022|Лабораторная работа №1: разбор типовых ошибок и изучение проблем реализации по падающим тестам.|[Видео урока](https://drive.google.com/file/d/15x-h2BvDy5_ISE9HMP_zAk2vVBQQh-k6/view?usp=sharing)|N/A|
|29.03.2022|Работа со словарями: создание, изменение, основные свойства. Инкрементальное ревью улучшений по лабораторной работе №1 |[Видео урока](https://drive.google.com/file/d/1f9aXXf4ebcZ7_gg4FwMBLBzDRMtHbrWJ/view?usp=sharing)|[Листинг](./seminars/03.29.2022/practice_6.py)|
|05.04.2022|Лабораторная работа №2: знакомство и необходимые инструкции.|[Видео урока](https://drive.google.com/file/d/107EBPWqfpPuABpLqDlCAVkPRupHAvFz1/view?usp=sharing)|N/A|
|12.04.2022|Занятие отменено из-за отсутствия кворума.|N/A|N/A|
|19.04.2022|f-строки и области видимости: локальная (local), объемлющая (enclosing), глобальная (global) и встроенная (builtin).|Видео урока пока нет|N/A|

## Литература

### Базовый уровень

1. Mark Lutz. 
   [Learning Python](https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730).
2. Хирьянов Тимофей Фёдорович. Видеолекции. 
   [Практика программирования на Python 3](https://www.youtube.com/watch?v=fgf57Sa5A-A&list=PLRDzFCPr95fLuusPXwvOPgXzBL3ZTzybY).
3. Хирьянов Тимофей Фёдорович. Видеолекции. 
   [Алгоритмы и структуры данных на Python 3](https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0).
4. [Official Python 3 documentation](https://docs.python.org/3/).

### Продвинутый уровень

1. Mark Lutz.
   [Programming Python: Powerful Object-Oriented Programming](https://www.amazon.com/Programming-Python-Powerful-Object-Oriented/dp/0596158106)
1. J. Burton Browning. 
   [Pro Python 3: Features and Tools for Professional Development](https://www.amazon.com/Pro-Python-Features-Professional-Development/dp/1484243846).


## Начало работы и работа с репозиторием

Работа над лабораторными работами должна производиться в персональных форках данного
репозитория. Подробнее о настройке окружения, запуске тестов и публикации своих результатов
в [отдельном документе](./CONTRIBUTING.md).
