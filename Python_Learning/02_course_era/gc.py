#!/usr/bin/python
"""
This is my frist Python program
It computees the GC content of DNA sequence.
"""
# get DNA sequence:
dna = input("input your dna sequence?")
dna = dna.lower()
no_c = dna.count('c') # count C's in DNA sequence
no_g = dna.count('g') # count G's in DNA sequence
dna_length = len(dna) # get the length of the DNA sequnce
gc_percent = (no_c+no_g)*100/dna_length # compute gc percentage
print(gc_percent) # print gc percnt
