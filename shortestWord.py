# Solution to https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
#Simple, given a string of words, return the length of the shortest word(s).

def find_short(s):
    words = s.split()
    shortest = min(words, key=len)
    return len(shortest)
