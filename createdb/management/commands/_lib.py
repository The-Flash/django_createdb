from typing import Mapping, Any


class BaseDBCreator:
    def __init__(self, config: Mapping[str, Any]):
        self.config = config

    def create(self):
        raise NotImplementedError("this method must be implemented in a child class")


class Sqlite3DBCreator(BaseDBCreator):
    def create(self):
        import sqlite3

        db_name: str = self.config["NAME"]
        conn = sqlite3.connect(db_name)
        conn.close()


class PostgreSQLDBCreator(BaseDBCreator):
    def create(self):
        import psycopg2

        name = self.config["NAME"]
        host = self.config["HOST"]
        user = self.config["USER"]
        password = self.config["PASSWORD"]
        port = self.config.get("PORT", None)

        if port is None:
            port = "5432"

        conn = psycopg2.connect(
            dbname="postgres",
            host=host,
            user=user,
            password=password,
            port=port,
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute('CREATE DATABASE "%s"', (name,))
        conn.close()


class MySQLDBCreator(BaseDBCreator):
    def create(self):
        import MySQLdb

        name = self.config["NAME"]
        host = self.config["HOST"]
        user = self.config["USER"]
        password = self.config["PASSWORD"]
        port = self.config.get("PORT", "3306")

        conn = MySQLdb.connect(host=host, user=user, password=password, port=port)
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {name}")
        conn.close()
