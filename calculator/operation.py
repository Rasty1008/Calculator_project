from sum import*
from subtraction import*
from mult import*
from division import*



def calcculate(x, y, operation):
    if operation == '+':
        return sum_numb(x, y)
    elif operation  == '-':
        return subtraction_numb(x, y)
    elif operation == '*':
        return mult_numb(x, y)
    elif operation == '/':
        return division_numb(x, y)
    
