# Solution to https://www.codewars.com/kata/546e2562b03326a88e000020
# square every digit of a number and concatenate them. For example, if we run 9119 through the function, 811181 will come out

def square_digits(num):
    result = ''
    for i in str(num):
        squared = int(i)**2
        result += str(squared)
        
    return int(result)
