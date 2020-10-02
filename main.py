#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
import numpy as np
import pandas as pd
from numpy import random

DIGITS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

SYMBOLS = {
    'plus': '+',
    'minus': '-',
    'dot': '.',
    'space': ' ',
}

CONTINUE = {
    "all",
    "camel"
}

l = [1,2,3]
l[1:3]

def main(string):
    iscaps = False
    capital = False
    camelcase = False
    firstword = True
    code = ""
    string = string.split()
    # print(string)
    for i, s in enumerate(string):
        if s in CONTINUE:
            continue
        # print(s)
        if i > 0 and " ".join(string[i-1:i+1]) == "all caps":
            iscaps = True
            capital = False
            camelcase = False
            continue
        if i > 0 and " ".join(string[i-1:i+1]) == "camel case":
            iscaps = False
            capital = False
            camelcase = True
            firstword = True
            continue
        if s == "capital":
            iscaps = False
            capital = True
            camelcase = False
            continue
        if s in DIGITS:
            code += DIGITS[s]
        elif s in SYMBOLS:
            code += SYMBOLS[s]
            iscaps = False
            capital = False
            camelcase = False
        else:
            if iscaps:
                code += s.upper()
                if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                    code += "_"
            elif capital:
                code += s[0].upper() + s[1:]
                if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                    code += " "
            elif camelcase:
                if firstword:
                    code += s
                else:
                    code += s[0].upper() + s[1:]
                if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                    code += ""
                firstword = False
            else:
                code += s
                if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                    code += " "
        # Handle escape
        # 'escape': '',
        # print('code')
        # print(code)
    return ''.join(code)



s1="a plus b"
s3="x one"
s4="a space plus space b"
s6="a plus"
s7="a plus b plus c"
s2="all caps foo bar plus bar"
s8="capital foo bar"

s5="index escape of"
s9="f of x plus one"
s10="f in angle brackets x plus one"
s11="foo of bar baz"
print(main(s2))


