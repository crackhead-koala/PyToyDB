from typing import *

from DatabaseSchema import DatabaseSchema
from Table import *


class Database:
    _name: str
    _schema: DatabaseSchema
    _tables: Dict[str, Table] = {}

    def __init__(self, name: str, schema_path: str) -> None:
        self._name = name
        self._schema = DatabaseSchema(schema_path, name)
        self._schema.update_schema()

    def create_table(self, name) -> None:
        self._tables[name] = Table(name)
        self._schema.add_table(name)
        self._schema.update_schema()
