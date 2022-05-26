# Solution to https://www.codewars.com/kata/514b92a657cdc65150000006
# Finish the program so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 

def solution(number):
    sum = 0
    for i in range(number):
        if i % 5 == 0:
             sum = sum + i
        elif i % 3 == 0:
            sum = sum + i
    
    return sum
