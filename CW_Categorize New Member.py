#Solution to https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
#CodeWars Categorize New Member, Difficulty 7kyu

#Instructions:
#Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
#Output will consist of a list of string values stating whether the respective member is to be placed in the senior or open category.


# if the first and second index meet the senior criteria, return senior. else return open
#Completion time: ~7 min

def open_or_senior(data):
    
    return[ "Senior" if x[0] >= 55 and x[1] > 7
        else "Open" for x in data]
