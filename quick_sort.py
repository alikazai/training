"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
      pivot = array[0]
      for x in array:
          if x < pivot:
              less.append(x)
          elif x == pivot:
              equal.append(x)
          elif x > pivot:
              greater.append(x)
      # Don't forget to return something!
      return quicksort(less) + equal + quicksort(greater)
      # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
      return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))