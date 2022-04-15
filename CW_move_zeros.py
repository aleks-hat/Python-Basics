#Link to problem: https://www.codewars.com/kata/52597aa56021e91c93000cb0
#Solution to Moving Zeros to the End
#Instructions: Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    
    index = 0
    list = []
    for i in array:
        if i == 0:
            index += 1
        else:
            list.append(i)
    for i in range(index):
        list.append(0)
    return list
