# Django CreateDB

This is a library that allows you to create databases based on settings.py DATABASES configurations.

Currently supported databases are:
* sqlite3
* postgresql
* mysql

it is equivalent to sequelize's ```sequelize-cli db:create```

## Installation

``` bash
pip install django-createdb
```

## Usage

1. Add INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = [
    ...
    createdb
    ...
]
```

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRESQL_NAME"),
        "HOST": env("POSTGRESQL_HOST"),
        "USER": env("POSTGRESQL_USER"),
        "PASSWORD": env("POSTGRESQL_PASSWORD"),
    },
    "mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("MYSQL_NAME"),
        "HOST": env("MYSQL_HOST"),
        "USER": env("MYSQL_USER"),
        "PASSWORD": env("MYSQL_PASSWORD"),
        "PORT": 3306,
    },
}
```

2. ```python manage.py createdb```
    This will create a database based on the "default" database settings

    You can specify which configuration to use by providing the ```--db``` argument

    ```
    python manage.py createdb --db postgresql
    ```
