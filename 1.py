#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    capitalized_words = [word.capitalize() for word in s.split(' ')]
    return ' '.join(capitalized_words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
