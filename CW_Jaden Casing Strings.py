#Jaden Casing Strings Solution, Level 7kyu Difficulty

#Instructions:
#Your task is to convert strings to how they would be written by Jaden Smith. 
#The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

#Completion time: ~6 min

def to_jaden_case(string):
    text = string.split(" ")
    jadenText = []
    for word in text:
        jadenText.append(word.capitalize())
        
    return " ".join(jadenText)
