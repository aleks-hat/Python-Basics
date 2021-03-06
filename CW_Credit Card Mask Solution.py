# CodeWars Python 7kyu Difficulty
# Solution to https://www.codewars.com/kata/5412509bd436bd33920011bc
#Your task is to write a function maskify, which changes all but the last four characters into '#'.
#Completion time: ~11 min

# if length of cc number is more than 4, replace all numbers except last 4
 
def maskify(cc):
    masked = ''
    if len(cc) > 4:
        masked += '#' * (len(cc) - 4) + cc[-4:]
        
    else:
        return cc
    
    return masked
 
    pass
