# Исходный код Django-проекта

Код из локальной папки `C:\Users\HOME\Desktop\MyProject` после выполнения ЛР1 и ЛР2.

## Структура

```text
MyProject/
├── requirements.txt
└── MySite/
    ├── manage.py
    ├── MySite/       # настройки и маршруты проекта
    ├── news/         # представления и маршруты ЛР1
    └── catalog/      # модель Product и миграции ЛР2
```

## Запуск в Windows PowerShell

В локальном проекте использованы Python 3.14.2 и Django 6.1.1. Команды ниже выполняются из этой папки `MyProject`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
cd MySite
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py runserver
```

После запуска доступны:

- [Hello world](http://127.0.0.1:8000/news/)
- [Тестовая страница](http://127.0.0.1:8000/news/test/)

Товары пока обрабатываются через Django shell; вывод каталога в браузер будет добавлен в ЛР3.

## Данные и настройки

В репозитории находятся исходники приложений и обе миграции `catalog`. Виртуальное окружение, кеш Python, настройки IDE и локальная SQLite-база исключены через `.gitignore`. Команда `migrate` создаст новую базу с таблицами; учебные товары в неё автоматически не добавляются. Команды создания товаров приведены в [отчёте ЛР2](../lab2/README.md).

В публикуемой копии `settings.py` исходный `SECRET_KEY` заменён: можно задать переменную окружения `DJANGO_SECRET_KEY`, иначе используется ключ для локальной разработки. Остальные исходники скопированы без изменений. Настройки `DEBUG=True` и запасной ключ предназначены для локального учебного запуска.
