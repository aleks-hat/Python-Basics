#Jaden Casing Strings Solution, Level 7kyu Difficulty
#Capitalize first word in a string
#Completion time: ~6 min

def to_jaden_case(string):
    text = string.split(" ")
    jadenText = []
    for word in text:
        jadenText.append(word.capitalize())
        
    return " ".join(jadenText)