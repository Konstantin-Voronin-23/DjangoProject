# Проект на Django |Онлайн  Магазин|

## Описание проекта

    - Использование Django 5.2

    - Стандартная архитектура проекта с отдельным приложением catalog для разделения функционала

    - Реализованы страницы “Главная” и “Контакты” с использованием маршрутов и шаблонов Django

    - Безопасность формы с CSRF-защитой

    - Поддержка миграций моделей

    - Использование именованных маршрутов для упрощения навигации

    - Настроены создинение с Postgres

    - Настроены базовые шаблоны

    - Все контроллеры переведены с FBV на CBV

    - Создано новое приложения для ведения блога

    - Добавлены счетчик просмотрел и редиректы согласно ТЗ


# **Установка**:

### Для работы приложения необходимо установить интерпретатор *poetry*:

```pip install --user poetry```

### Так же клонируйте репозиторий:

```git clone https://github.com/Konstantin-Voronin-23/Project1.git```

# **Установка зависимостей**:

### Для работы проекта воспользуйтесь командами для установок зависимостей:

```
poetry add --group lint flake8
poetry add --group lint mypy
poetry add --group lint black
poetry add --group lint isort

poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add python-dotenv
poetry add requests
poetry add pandas
poetry add openpyxl
pip install psycopg2
poetry add django
poetry add Pillow
poetry add ipython


```

# Документация

# Лицензия

## - Этот проект лицензирован по [лицензии MIT](LICENSE).