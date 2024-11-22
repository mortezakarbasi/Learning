#!/usr/bin/python
"""
This is my second program
it will get dna from you and reverse dna
"""
dna = list(input("please enter your dna sequence? "))
dna_reverse = dna[::-1]
dna_reverse_string = "".join(dna_reverse)
print(dna_reverse_string)
