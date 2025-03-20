'''
🔹 Problem 3: Sum of Digits
Write a function that takes a non-negative integer and returns the sum of its digits.
Example:
🔹 Input: 1234
🔹 Output: 10
💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.
'''
def sum_digit(n: str) -> int:
    count_sum: int = 0
    for i in n:
        count_sum += int(i)
    return count_sum

x = input('Enter an integer: ')
print(sum_digit(x))