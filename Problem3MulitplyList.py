#Syed Hussain
#08/20/2022
#Problem number 3 - A Python function to multiply all the numbers in a list. list [5, 2, 7, -1]
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((5, 2, 7, -1)))

