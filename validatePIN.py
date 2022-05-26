# Solution to https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
# PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true.

def validate_pin(pin):

    if pin.isnumeric() == False:
        return False
    elif len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
