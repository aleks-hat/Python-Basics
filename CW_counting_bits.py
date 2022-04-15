#Instructions: Write a function that takes an integer as input, and 
#returns the number of bits that are equal to one in the binary representation of that number.

# Link to problem: https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
#Solution for CodeWars Counting Bits problem 6kyu

def count_bits(n):
    count = 0
    while(n):
        count += n & 1
        n >>= 1
    return count
