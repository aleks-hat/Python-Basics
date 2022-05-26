# Solution to https://www.codewars.com/kata/515e271a311df0350d00000f
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

import numpy as np

def square_sum(numbers):
    print(numbers)
    squared = np.square(numbers)
    print(squared)
    sumSquared = sum(squared)
    return sumSquared
    
