# textcounts
Python library for counting lines of text

## Requirements

pandas (and its dependencies), python 2.7 or 3.3 and up

## Installation

```
pip install textcounts
```

## Usage
### Import
```
import textcounts

list_of_strings = ["test one",
                   "test two",
                   "test three",
                   "test three point one",
                   "point"]
```
### Proportion of items matching a string
```
In [3]: textcounts.prop_mentions(list_of_strings, "test")
Out[3]: 0.8
```
### Proportion of items matching any string from a list of strings
```
In [4]: textcounts.prop_mentions(list_of_strings, ["one", "two"])
Out[4]: 0.6
```
### For each item, count number of times a string is found
```
In [5]: textcounts.pattern_counts(list_of_strings, ["one", "two"])
Out[5]: 

| location | one count | two count |
|----------|-----------|-----------|
| 0        | 1         | 0         |
| 1        | 0         | 1         |
| 2        | 0         | 0         |
| 3        | 1         | 0         |
| 4        | 0         | 0         |
```
### For each item, count number of times sets of strings are found
Note: use a dict of `{string label : list of strings to match}` to group patterns
```
In [6]: pattern_dict = {"numbers" : ["one", "two", "three"],
                        "odd numbers" : ["one", "three"],
                        "test" : ["test"]}

In [7]: textcounts.pattern_counts(list_of_strings, pattern_dict)
Out[7]: 

| location | numbers count | odd numbers count | test count |
|----------|---------------|-------------------|------------|
| 0        | 1             | 1                 | 1          |
| 1        | 1             | 0                 | 1          |
| 2        | 1             | 1                 | 1          |
| 3        | 2             | 2                 | 1          |
| 4        | 0             | 0                 | 0          |

```
