#Link to problem: https://www.codewars.com/kata/525f50e3b73515a6db000b83
#Solution to CodeWars Create Phone Number
#Instructions: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    
    num = '('
    for i, j in enumerate(n):
        if i < 3:
            num += str(j)
            if i == 2:
                num += ') '
        elif i <= 10:
            num += str(j)
            if i == 5:
                num += '-'
    return num
