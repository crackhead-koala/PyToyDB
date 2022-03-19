from typing import Dict, Any
import json


class DatabaseSchema:
    _path: str
    _structure: Dict[str, Any] = {}

    def __init__(self, path: str, database_name: str) -> None:
        self._path = path
        self._structure['database'] = database_name
        self._structure['tables'] = []

    def update_schema(self) -> None:
        name = self._structure['database']
        with open(f'{self._path}/{name}_PyToyDBSchema.json', 'w') as outfile:
            outfile.write(json.dumps(self._structure))

    def add_table(self, name: str) -> None:
        self._structure['tables'].append(name)
