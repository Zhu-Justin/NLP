#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
from main import NLP 

# The fun begins!
# Test cases
s1="a plus b"
s2="all caps foo bar plus bar"
s3="capital foo bar"
s4="x one"
s5="a space plus space b"
s6="f of x plus one"
s7="f in angle brackets x plus one"
s8="foo of bar baz"
s9="index escape of"
s10="a plus"
s11="a plus b plus c"

tests = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]

for text in tests:
    print(text + " -> " + str(NLP(text)))

