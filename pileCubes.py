# Solution to https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

def find_nb(m):
    total = 0
    n = 0
    
    while total < m:
        n = n + 1
        total = total + pow(n, 3)
    
    if total == m:
        return n
    else: 
        return -1
