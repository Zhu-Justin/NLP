#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
from enum import Enum

class Case(Enum):
    NORMAL = 0
    ALLCAPS = 1
    CAMEL = 2
    CAPITAL = 3
    ESCAPE = 4

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

class NLP():
    def __init__(self, text, digits=DIGITS, symbols=SYMBOLS):
        self.text = text
        self.digits = digits
        self.symbols = symbols
        self.code = ""
        self.state = Case.NORMAL

# def main(string):
        # iscaps = False
        # capital = False
        # camelcase = False
        firstword = True
        # code = ""
        string = self.text.split()
        # print(string)
        for i, s in enumerate(string):
            if s in CONTINUE:
                continue
            # print(s)
            if i > 0 and " ".join(string[i-1:i+1]) == "all caps":
                self.state = Case.ALLCAPS
                # iscaps = True
                # capital = False
                # camelcase = False
                continue
            if i > 0 and " ".join(string[i-1:i+1]) == "camel case":
                self.state = Case.CAMEL
                # iscaps = False
                # capital = False
                # camelcase = True
                firstword = True
                continue
            if s == "capital":
                self.state = Case.CAPITAL
                # iscaps = False
                # capital = True
                # camelcase = False
                continue
            if s in DIGITS:
                self.code += DIGITS[s]
            elif s in SYMBOLS:
                self.code += SYMBOLS[s]
                self.state = Case.NORMAL
                # iscaps = False
                # capital = False
                # camelcase = False
            else:
                # if iscaps:
                if self.state == Case.ALLCAPS:
                    self.code += s.upper()
                    if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                        self.code += "_"
                # elif capital:
                elif self.state == Case.CAPITAL:
                    self.code += s[0].upper() + s[1:]
                    if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                        self.code += " "
                # elif camelcase:
                elif self.state == Case.CAMEL:
                    if firstword:
                        self.code += s
                    else:
                        self.code += s[0].upper() + s[1:]
                    if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                        self.code += ""
                    firstword = False
                else:
                    self.code += s
                    if i + 1 < len(string) and string[i + 1] not in {**SYMBOLS, **DIGITS}:
                        self.code += " "
            # Handle escape
            # 'escape': '',
            # print('code')
            # print(code)
        # return ''.join(self.code)



# Test cases
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
# print(main(s2))
x = NLP(s7)
x = NLP(s2)
x = NLP(s8)
x.code


# print(Case.CAPS)
# Case.CAPS == "all caps"
# Case.CAPS == 'all caps'
# # Case['all caps'] == 
# print(repr(Case.CAPS))
