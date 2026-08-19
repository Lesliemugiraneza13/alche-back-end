# API

Scripts that gather employee TODO list data from the JSONPlaceholder REST
API (https://jsonplaceholder.typicode.com) and export it in different
formats.

## Requirements

- Interpreted/compiled on Ubuntu 14.04 LTS with python3 (3.4.3)
- All files start with `#!/usr/bin/python3` and are executable
- PEP 8 compliant, imports alphabetically ordered
- Every module is documented
- Uses `dict.get()` to safely access dictionary values
- Code only runs when the script is executed directly
  (`if __name__ == "__main__":`)
- Requires the `requests` library (`pip3 install requests`)

## Tasks

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Prints an employee's TODO progress and completed task titles |
| `1-export_to_CSV.py` | Same as task 0, plus exports all of that employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports one employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

```
./0-gather_data_from_an_API.py <employee_id>
./1-export_to_CSV.py <employee_id>
./2-export_to_JSON.py <employee_id>
./3-dictionary_of_list_of_dictionaries.py
```
