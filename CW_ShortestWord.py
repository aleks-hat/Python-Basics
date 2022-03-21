#Solution in response to https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
#CodeWars Shortest Word, Level 7kyu Difficulty
#Instructions:
#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

#WORK IN PROGRESS

#for every string in the list, if length of next string is less than the length of initial string, set the intial length eaqul to new one

def find_short(s):
    length = len(s)
    short = len(s[0])
    index = 0
    for x in range(1, length):
        if len(s[x]) < short:
            short = s[x]
            index = x
    return index 
# returns the index of the shortest word in the list
