#Link to problem: https://www.codewars.com/kata/5842df8ccbd22792a4000245
#Solution to Write Number in Expanded Form
#Instructions:  For example: expanded_form(12) # Should return '10 + 2' , expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    num = str(num)
    index = []
    
    for i, j in enumerate(num[::-1]):
        if int(j) != 0:
            index.append(j + ('0' * i))

    return ' + '.join(index[::-1])
    pass
