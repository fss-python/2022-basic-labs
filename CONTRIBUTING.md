# Работа с репозиторием

## Запуск тестов

Для запуска тестов выполните следующую команду в папке с лабораторной работой:

```bash
python -m pip install pytest
python -m pytest -m lab_1
```

## Что делать если в родительском репозитории есть изменения и они мне нужны?

1. Создаем `upstream` таргет в репозитории:

```bash
git remote add upstream https://github.com/fss-python/2022-basic-labs-admin
```

2. Получаем данные об изменениях в удаленном репозитории:

```bash
git fetch upstream
```

3. Обновляем свой репозиторий с изменениями из удаленного репозитория:

```bash
git merge upstream/master
```

## Проверка орфографии

1. Установить зависимости 
   [инструмента для проверки](https://facelessuser.github.io/pyspelling/#usage-in-linux). 
   Например, для macOS:

   ```bash
   brew install aspell
   ```

1. Установить зависимости для Python:

   ```bash
   python -m pip install -r requirements_qa.txt
   ```

1. Запуск проверки:

   ```bash
   python -m pyspelling -c automation/spellcheck/.spellcheck.yaml
   ```