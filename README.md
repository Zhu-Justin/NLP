# NLP

A primitive Natural Language Processor that converts standard English syntax into code.

## Features

1.  Default style is lower case with spaces between words. Other styles include "all caps", "camel case", "capital".
2.  Converts integers from English to numeric form (0-9)
3.  Converts symbols from English (minus, plus, dot, space) to actual symbols ("-", "+", ".", " ")
4.  Adds parenthesis using the keyword "of" and angle brackets using the keyword "in angle brackets"
5.  Supports escape in the text to escape special keywords like "of"
6.  Symbols and numbers are "sticky", i.e. no excess whitespace surrounding symbols and numbers unless "space" is explicitly specified

## Files 

1.  `test.py` - User runs this file and modifies test cases as desired!
2.  `main.py` - Main class

# Getting started

```
git clone https://github.com/Zhu-Justin/NLP.git /path/to/repo

cd /path/to/repo

./test.py
```

# Getting help

```
python3
>>> from main import NLP
>>> help(NLP)
```

# Notes

The `NLP` object requires just one argument, which is the text you want to convert to code. `test.py` has some demos you can play around with!

