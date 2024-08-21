import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, DefaultDict, Iterator, Optional


@dataclass(frozen=True, slots=True)
class CASEntry:
    """
    Represents a chemical substance identified by its CAS (Chemical Abstracts Service) number.

    Attributes:
        cas (str): The CAS number of the chemical substance, a unique identifier used globally.
        name (str): The common name of the chemical substance.
        formula (str): The molecular formula of the chemical substance.
    """

    cas: str
    name: str
    formula: str


class CASDatabase:
    """
    A class representing a database of chemical substance entries indexed by CAS number, name, and molecular formula.

    Attributes:
        _cas_entries (list[CASEntry]): A list of CASEntry objects representing the database entries.
        _inverted_index (defaultdict): A dictionary that maps fields (cas, name, formula) to corresponding CASEntry objects.

    Methods:
        get(default: Optional[Any] = None, **kw: Optional[str]):
            Retrieves a CASEntry object based on a specified field (cas, name, or formula).
            Raises TypeError if more than one field is provided.
            Raises LookupError if the value provided is not a string.

        __iter__() -> Iterator["CASDatabase"]:
            Returns an iterator over the CASEntry objects in the database.

        __len__() -> int:
            Returns the number of CASEntry objects in the database.
    """

    def __init__(self, database_path: Path):
        with open(database_path, encoding="utf-8") as f:
            db_json = json.load(f)

        self._cas_entries = []
        self._inverted_index: DefaultDict[str, dict] = defaultdict(dict)
        for entry in db_json:
            cas_entry = CASEntry(**entry)
            self._cas_entries.append(cas_entry)

            for key, value in entry.items():
                self._inverted_index[key][value] = cas_entry

    def get(self, default: Optional[Any] = None, **kw: Optional[str]):
        if len(kw) != 1:
            raise TypeError("Only one of (cas, name, formula) may be given")

        field, value = kw.popitem()
        if not isinstance(value, str):
            raise LookupError(f"Value for {field} needs to be str")

        return self._inverted_index.get(field, {}).get(value, default)

    def __iter__(self) -> Iterator["CASEntry"]:
        return iter(self._cas_entries)

    def __len__(self) -> int:
        return len(self._cas_entries)
