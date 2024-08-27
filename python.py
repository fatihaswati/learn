# Problem: Given a list of numbers, count how many are positive and negative numbers.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positiveNum = 0
for sum in numbers:
    if sum > 0:
        positiveNum += 1
print("Positive numbers in this list are", positiveNum)

negativeNum = 0 
for neg in numbers:
    if neg < 0:
        negativeNum += 1
print(f"This list contain {negativeNum} numbers")