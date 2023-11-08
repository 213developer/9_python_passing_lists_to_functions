"""
Reverse.py - This program reverses numbers stored in an array.
Input: Interactive.
Output: Original contents of array and the reversed contents of the array.
"""
result = []

# Write reverseArray function here.
def reverseArray(array):
    reverse = []
    for i in range(len(array),0,-1):
        reverse.append(array[i-1])
    return reverse

numbers = [9, 8, 7, 6, 5]

# Print contents of array.
print("Original contents of array:")
for item in numbers:
    print(item)
# Call reverseArray function here.
result = reverseArray(numbers)
# Print contents of reversed array.
print("Reversed contents of array:")
for item in result:
    print(item)
