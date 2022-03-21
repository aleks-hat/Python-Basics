#Highest and Lowest Solution, Level 7kyu Difficulty

#Instructions:
#You are given a string of space separated numbers, and have to return the highest and lowest number.
#Notes: 
#All numbers are valid
#There will always be at least one number in the input string.
#Output string must be two numbers separated by a single space, and highest number is first.

#for numbers given, if number is higher than known highest number
# replace until highest num is found, then print - same with lowest number
#Completion time: ~ 12 min

def high_and_low(numbers):
        numbers = numbers.split(" ")
        highest_number = numbers[0]
        lowest_number = numbers[0]
    
        for temp in numbers:
            if int(temp) > int(highest_number):
                highest_number = temp
            if int(temp) < int(lowest_number):
                lowest_number = temp
                
        return highest_number + " " + lowest_number
