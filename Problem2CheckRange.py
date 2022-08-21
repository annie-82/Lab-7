#Syed Hussain
#08/20/2022
#Problem number 2 - A Python function to check whether a number is in a given range. Using range(1,10).
# Print whether the number is in or not in the rang

def test_range(n):
    if n in range(1,10):
        print(n,"is in the range")
    else:
        print(n,"is not in a range")
test_range(5)
