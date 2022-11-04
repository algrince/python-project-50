### Hexlet tests and linter status:
[![Actions Status](https://github.com/algrince/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/algrince/python-project-50/actions)
[![Python CI](https://github.com/algrince/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/algrince/python-project-50/actions/workflows/pyci.yml)
### Codeclimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/c4b4a365cf37997e7de3/maintainability)](https://codeclimate.com/github/algrince/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c4b4a365cf37997e7de3/test_coverage)](https://codeclimate.com/github/algrince/python-project-50/test_coverage)

## Description
Gendiff is a CLI utility that compares two files and generates an output that shows the difference. The comparision can be made between .json and .yaml files. The input files can have the different extension.

The output can be printed in 3 different styles, which can be chosen when calling the utility. The default style is 'stylish'. The output supports recursive data.

### 'Stylish' style
- Every group of properties is included in `{}`
- The stantard indentation is 4
- One space before the key (included in identation) `+` or `-` is placed if the property is added or removed
- If property is updated, diff includes removed line and the added one (in ths order)
<details>
  <summary>Stylish output</summary>
```
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
```
</details>


### 'Plain' style
- Added property are included indicating the value
- Removed properties are included as removed
- If the value of a property changes, it is included as updated with both new and old values
- If the value of property is nested, it is replaced with `[complex value]`.
- If property is nested, its key is merged with all its parent keys including root.
- Property withiout change is not dispayed. 
<details>
  <summary>Plain output</summary>
```
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```
</details>

### 'JSON' style
- Data is formatted in JSON style.
- Added property has child dictionary where key states 'added' and value contains property's value.
- Removed property is handled in the same way as added. A key in child dictionary is 'removed'.
- Updated property is shown with both 'added' and 'removed' lines in child dictionary.
- Propierty that has suffered no changes if displayed without any correction.
<details>
  <summary>JSON output</summary>
```
{
    "common": {
        "follow": {
            "added": false
        },
        "setting1": "Value 1",
        "setting2": {
            "removed": 200
        },
        "setting3": {
            "removed": true,
            "added": null
        },
        "setting4": {
            "added": "blah blah"
        },
        "setting5": {
            "added": {
                "key5": "value5"
            }
        },
        "setting6": {
            "doge": {
                "wow": {
                    "removed": "",
                    "added": "so much"
                }
            },
            "key": "value",
            "ops": {
                "added": "vops"
            }
        }
    },
    "group1": {
        "baz": {
            "removed": "bas",
            "added": "bars"
        },
        "foo": "bar",
        "nest": {
            "removed": {
                "key": "value"
            },
            "added": "str"
        }
    },
    "group2": {
        "removed": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "added": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}
```
</details>

## Instalation
Please note that there was no publication made fo this package. The instalation can be made following these steps:
1. Clone the repository:
`git clone https://github.com/algrince/python-project-50.git`
2. Go to the project folder:
`cd python-project-50`
3. Proceed to the setup:
`make setup`

## Usage
The utility can be used in command line...
```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows the difference

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: stylish)
```
... and also as part of the library:
```
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```