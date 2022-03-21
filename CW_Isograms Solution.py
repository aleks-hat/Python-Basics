#Solution to https://www.codewars.com/kata/54ba84be607a92aa900000f1

# CodeWars Isograms, 7 kyu Difficulty
# Instructions:
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# if letter is in alphabet and is reused return false, else return true
#Completion time: ~15 min

def is_isogram(word):
    
    new_word = word.lower()
    used_letters = []
    
    for letter in new_word:
        if letter.isalpha():
            if letter in used_letters:
                return False
            used_letters.append(letter)
            
    return True
