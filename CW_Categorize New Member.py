#CodeWars Categorize New Member Solution, Difficulty 7kyu
# if the first and second index meet the senior criteria, return senior. else return open
#Completion time: ~7 min

def open_or_senior(data):
    
    return[ "Senior" if x[0] >= 55 and x[1] > 7
        else "Open" for x in data]