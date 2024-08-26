# cas-python

cas-python is a Python library that provides access to a database of CAS Registry Numbers, allowing easy retrieval of chemical information by CAS number, chemical formula, or name.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cas-python.

```bash
pip install cas-python
```

## Usage

```python
>>> import cas

>>> # Get entry by CAS number
>>> cas.database.get(cas="7732-18-5")
CASEntry(cas='7732-18-5', name='water', formula='H2O')

>>> # Get entry by chemical formula
>>> cas.database.get(formula="H2O")
CASEntry(cas='7732-18-5', name='water', formula='H2O')

>>> # Get entry by chemical name
>>> cas.database.get(name="water")
CASEntry(cas='7732-18-5', name='water', formula='H2O')

>>> # Explore the retrieved entry
>>> gold = cas.database.get(name="gold")
>>> gold
CASEntry(cas='7440-57-5', name='gold', formula='Au')

>>> # Access specific attributes of the entry
>>> gold.cas
'7440-57-5'
>>> gold.formula
'Au'
```
