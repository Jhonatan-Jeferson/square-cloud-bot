from typing import Any


class MongoDB:
    """
    MongoDB Database object
    """

    instance = None

    def __init__(self, connection: str):
        from pymongo import MongoClient

        self.__connection = MongoClient(connection)
        self._users = self.__connection.get_database(
            'squarecloud'
        ).get_collection('Users')
        self._teams = self.__connection.get_database(
            'squarecloud'
        ).get_collection('Teams')

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(cls).__init__(*args, **kwargs)
        return cls.instance

    def get_user_token(self, user: int) -> dict[str, Any]:
        """Gets user square cloud API token from database"""
        query = {'_id': user}
        result = self._users.find_one(query)
        return result

    def register_user_token(self, user: int, token: str) -> None:
        """Sets user square cloud API token on database"""
        document = {'_id': user, 'squareApiToken': token}
        self._users.insert_one(document)

    def register_team(self, name: str, owner: int):
        """Sets a team to manage the application"""
        raise NotImplementedError('Not developed yet!')


class SQLDatabase:
    """Local SQL database object"""

    instance = None

    def __init__(self):
        import sqlite3 as db
        from os import path

        db_path = path.relpath(__file__)
        db_path = db_path[:-3] + '.db'
        self.__connection = db.connect(db_path)
        self._cursor = self.__connection.cursor()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(cls).__init__()
        return cls.instance

    def get_user_token(self, user: int):
        """Gets user square cloud API token from database"""
        query = self._cursor.execute(
            'SELECT * FROM TABLE Users WHERE user=?', (user,)
        )

    def register_user_token(self, user: int, token: str):
        """Sets user square cloud API token on database"""
        pass


class Database:
    """Generates a database based on args you pass"""

    def __new__(cls, connection: str | None = None) -> SQLDatabase | MongoDB:
        if connection is None:
            return SQLDatabase()
        else:
            return MongoDB(connection)
