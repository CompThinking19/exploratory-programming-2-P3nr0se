#defined how positive function to determine how many positives there are in the list
def howpositive(numbers):
    if type(numbers) != list:
        raise TypeError("Not a list!")
    positives = 0
    for element in list:
        if (element > 0):
            positives += 1
    return positives
# Calling howpositive with a list
howpositive([1])
#Calling howpositive with a string
howpositive("1")
