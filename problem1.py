'''
🔹 Problem 1: Reverse a String
Write a function that takes a string as input and returns the reversed string.
Example:
🔹 Input: "hello"
🔹 Output: "olleh"
💡 Hint: Use Python's slicing feature.
'''

def rev(s: str) -> str:
    '''Returns a reversed string'''
    return s[::-1]

x: str = input('Enter a text (string): ')
print(rev(x))