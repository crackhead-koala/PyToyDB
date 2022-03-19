from typing import Dict

from Database import Database


class Terminal:
    _databases: Dict[str, Database] = {}

    def __init__(self) -> None:
        print('Welcome to PyToyDB terminal.')

    def create_database(self, name: str, schema_path: str) -> None:
        self._databases[name] = Database(name, schema_path)

    def create_table(self, database: str, name: str) -> None:
        self._databases[database].create_table(name)
