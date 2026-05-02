# Python - Basic Serialization

This project covers the fundamentals of data serialization and deserialization using Python's `json` module.

## Learning Objectives
* Understand the difference between Marshaling and Serialization.
* Learn how to convert Python dictionaries into JSON files.
* Learn how to reconstruct Python objects from stored JSON data.

## Files
| File | Description |
| --- | --- |
| `task_00_basic_serialization.py` | Contains functions to save and load JSON data. |

## Usage
To use the serialization module:
```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {"name": "Alice", "job": "Engineer"}
serialize_and_save_to_file(data, 'example.json')

new_data = load_and_deserialize('example.json')
print(new_data)
