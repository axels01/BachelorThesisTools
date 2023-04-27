'''
Axel Östergren 2023-04-26

This is a short script to generate a random file tree
from a few set perameters. This script is written 
as part of a bachelor thesis project
by Axel Östergren and Arvid Albinsson at Högskolan Väst
in Trollhättan, Sweden.

The script is free to use and can be modified
by anyone. The script is provided as is and the authors
take no responsibility for any damage caused by the script.
'''

import random
import string

def generateCode(letterCount, numberCount, splitter = ''):
    letters = ''.join(random.choices(string.ascii_uppercase, k=letterCount))
    numbers = ''.join(random.choices(string.digits, k=numberCount))
    return letters + splitter + numbers

if __name__ == '__main__':
    print(generateCode(3, 3, '-'))