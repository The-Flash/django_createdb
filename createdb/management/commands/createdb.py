from typing import Type

from django.conf import settings
from django.core.management.base import BaseCommand

from ._lib import BaseDBCreator, MySQLDBCreator, PostgreSQLDBCreator, Sqlite3DBCreator

from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = "Create database based on settings.py"

    cls_mapping: dict[str, Type[BaseDBCreator]] = {
        "django.db.backends.sqlite3": Sqlite3DBCreator,
        "django.db.backends.postgresql": PostgreSQLDBCreator,
        "django.db.backends.mysql": MySQLDBCreator,
    }

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--db", default="default", type=str)

    def handle(self, *args, **kwargs):
        selected_db_arg = kwargs["db"]
        DB_SETTINGS = settings.DATABASES
        config = DB_SETTINGS[selected_db_arg]

        engine = config["ENGINE"]

        cls = self.cls_mapping[engine]
        db_creator = cls(config)
        db_creator.create()
        self.stdout.write(self.style.SUCCESS("Successfully created database"))
