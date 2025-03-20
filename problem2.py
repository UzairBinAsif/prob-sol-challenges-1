'''
🔹 Problem 2: Count Vowels in a String
Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
Example:
🔹 Input: "Apple"
🔹 Output: 2
💡 Hint: Use a loop and check if each character is in a set of vowels.
'''
def vowel(s: str) -> int:
    '''Returns the number of vowels present in a given string'''
    count_vowel: int = 0
    set_of_vowel: list = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i.lower() in set_of_vowel:
            count_vowel += 1
    return count_vowel

x: str = input('Enter text: ')
print('No. of vowels:', vowel(x))