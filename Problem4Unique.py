#Syed Hussain
#08/20/2022
#Problem number 4 - A Python function that takes a list of numbers and returns a new list with unique elements of the first list.
# Using list [1, 3, 3, 3, 6, 2, 3, 5].
# Using the appendfunction

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))
