#Printer Errors Solution, Level 7kyu Difficulty
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