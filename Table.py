from typing import List, Any


class TableColumn:

    def __init__(self, data: List[Any], data_type: str) -> None:
        pass


class PrimaryKeyColumn(TableColumn):
    pass


class SecondaryKeyColumn(TableColumn):
    pass


class IntegerTableColumn(TableColumn):
    pass


class FloatTableColumn(TableColumn):
    pass


class StringTableColumn(TableColumn):
    pass


class BooleanTableColumn(TableColumn):
    pass


class Table:
    _name: str

    def __init__(self, name) -> None:
        self._name = name
