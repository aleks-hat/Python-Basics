# CodeWars Isograms Solution, 7 kyu Difficulty
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
