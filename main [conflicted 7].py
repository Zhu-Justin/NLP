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
        self.code = ""
        self.state = Case.NORMAL
        # User can modify DIGITS and SYMBOLS dictionaries
        DIGITS = digits
        SYMBOLS = symbols
        self.special = {**SYMBOLS, **DIGITS}
        self.parenthesis = []

        firstword = True
        string = self.text.split()
        for i, s in enumerate(string):
            if self.skip(i, string):
                continue
            if self.getcase(i, string) == "escape":
                self.state = Case.ESCAPE
                continue
            if self.getcase(i, string) == "all caps":
                self.state = Case.ALLCAPS
                continue
            if self.getcase(i, string) == "camel case":
                self.state = Case.CAMEL
                firstword = True
                continue
            if self.getcase(i, string) == "capital":
                self.state = Case.CAPITAL
                continue
            # if self.state != Case.ESCAPE:
            if self.paren(i, string) == "<>":
                self.code = self.code[:-1]
                self.code += "<"
                self.parenthesis.append(">")
                continue
            if self.paren(i, string) == "()":
                self.code = self.code[:-1]
                self.code += "("
                self.parenthesis.append(")")
                continue
            if s in DIGITS:
                self.code += DIGITS[s]
            elif s in SYMBOLS:
                self.code += SYMBOLS[s]
                self.state = Case.NORMAL
            else:
                if self.state == Case.ALLCAPS:
                    self.code += s.upper()
                    if self.includespace(i,string):
                        self.code += "_"
                elif self.state == Case.CAMEL:
                    if firstword:
                        self.code += s
                    else:
                        self.code += s[0].upper() + s[1:]
                    if self.includespace(i, string):
                        self.code += ""
                    firstword = False
                else:
                    if self.state == Case.CAPITAL:
                        self.code += s[0].upper() + s[1:]
                    else:
                        self.code += s
                    if self.includespace(i, string):
                        self.code += " "
        self.code += ''.join(self.parenthesis)

    # Helper functions
    def skip(self, index, string):
        # decide if we should skip the word
        if index + 1 < len(string):
            keyword = ' '.join(string[index:index + 2])
            if keyword in ["all caps", "camel case"]:
                return True
        if index + 2 < len(string):
            keyword = ' '.join(string[index:index + 3])
            if keyword in ["in angle brackets"]:
                return True
        if index + 2 < len(string) and index > 0:
            keyword = ' '.join(string[index-1:index + 2])
            if keyword in ["in angle brackets"]:
                return True
        return False

    def getcase(self, index, string):
        # get the word if it denotes a case
        if index > 0:
            return " ".join(string[index-1:index+1])
        return string[index]

    def includespace(self,index, string):
        # return True we should include a space
        return index + 1 < len(string) and string[index + 1] not in self.special

    def paren(self, index, string):
        if index - 1 > 0:
            keyword = ' '.join(string[index-2:index + 1])
            if keyword in ["in angle brackets"]:
                return "<>"
        if index > 0 and string[index] == "of":
            return "()"
        return False


# Now the fun begins!
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
x = NLP(s9)
x = NLP(s10)
x = NLP(s11)
x = NLP(s11)
x = NLP(s5)
x.code


# print(Case.CAPS)
# Case.CAPS == "all caps"
# Case.CAPS == 'all caps'
# # Case['all caps'] == 
# print(repr(Case.CAPS))
