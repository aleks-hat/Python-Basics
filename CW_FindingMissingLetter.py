#Solution to https://www.codewars.com/kata/5839edaa6754d6fec10000a2
#Finding the Missing Letter, 6kyu Difficulty

#Instructions:
#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#WORK IN PROGRESS

def find_missing_letter(chars):
    
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alpha.find(chars[0])
    
    comp = alpha[index:index+len(chars)+1]

    for e, i in enumerate(comp):
        if chars[e] != comp[e]:
            return comp[e]
