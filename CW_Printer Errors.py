#Solution to https://www.codewars.com/kata/56541980fa08ab47a0000040
#CodeWars Printer Errors, Level 7kyu Difficulty

#Instructions:
#You have to write a function printer_error which given a string will return the error rate of the printer as a string representing 
#rational whose numerator is the number of errors and the denominator the length of the control string. 
#Don't reduce this fraction to a simpler expression.
#The string has a length greater or equal to one and contains only letters from a to z.

#if letter not in given color range, add error. else good.
#Completion time: ~9 min

colors = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

def printer_error(s):
    s_length = len(s)
    error = int()
    for letters in s:
        if letters not in colors:
            error = error + 1
        else:
            pass
        
    print("s = " + str(s))
    print("printer_error(s) => " + str(error) + "/" + str(s_length))
    
    return (str(error) + "/" + str(s_length))
