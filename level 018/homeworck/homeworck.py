num1 = 5
num2 = 10
sum_result = num1 + num2
print("Sum:", sum_result)


str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated version:", concatenated_str)


a = 7
b = 3
division_result = a / b
print("Division result:", division_result)


x = 5
y = 10
print(x < y)  # True


x = 10
y = 5
print(x > 5 and y < 10)  # True
print(x == 10 or y > 10)  # True
print(not (x < 5))  # True
print((x + y) == 15 and y != 5)  # False
print(x > 0 or y < 0)  # True


for i in range(1, 11):
    print(i)


numbers = [1, 3, 4, 5, 2]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print("Sum:", sum_of_numbers)


text = "Hello, World!"
for char in text:
    print(char)


i = 1
while i <= 10:
    print(i)
    i += 1


i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1


total = 0
i = 1
while total < 50:
    total += i
    i += 1
print("Total:", total)


def check_divisibility(num):
    if num % 3 == 0 or num % 5 == 0:
        print(f"{num} is divisible by 3 or 5")
    else:
        print(f"{num} is not divisible by 3 or 5")

check_divisibility(15)


def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 3, 4, 5, 2]))  # output: 3
def every_second_upper(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

print(every_second_upper("hello"))  # output: HeLlO


def square_list(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

print(square_list([3, 12, 5, 2, 6]))  # output: [9, 144, 25, 4, 36]


def capitalize_every_second(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

print(capitalize_every_second("hello"))  # output: HeLlO


def square_list(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

print(square_list([3, 12, 5, 2, 6]))  # output: [9, 144, 25, 4, 36]


# 1. Sum of two int variables
num1 = 5
num2 = 10
sum_result = num1 + num2
print("Sum:", sum_result)

# 2. Concatenation of two str variables
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated version:", concatenated_str)

# 3. Division of int variables
a = 7
b = 3
division_result = a / b
print("Division result:", division_result)

# 4. Example of comparison operator
x = 5
y = 10
print(x < y)  # True

# 5. Combination of mathematical and comparison operators
result = 5 + 5 == 8 + 2
print(result)  # True

# 6. Logical operator combinations
x = 10
y = 5
print(x > 5 and y < 10)  # True
print(x == 10 or y > 10)  # True
print(not (x < 5))  # True
print((x + y) == 15 and y != 5)  # False
print(x > 0 or y < 0)  # True

# 7. For loop from 1 to 10
for i in range(1, 11):
    print(i)

# 8. Sum of numbers in a list
numbers = [1, 3, 4, 5, 2]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print("Sum:", sum_of_numbers)

# 9. Print each character in a string
text = "Hello, World!"
for char in text:
    print(char)

# 10. While loop from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 11. While loop to skip numbers from 50 to 60
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

# 12. While loop to accumulate sum until it reaches 50
total = 0
i = 1
while total < 50:
    total += i
    i += 1
print("Total:", total)

# 13. Check if a number is divisible by 3 or 5
def check_divisibility(num):
    if num % 3 == 0 or num % 5 == 0:
        print(f"{num} is divisible by 3 or 5")
    else:
        print(f"{num} is not divisible by 3 or 5")

check_divisibility(15)

# 14. Calculate average of a list
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 3, 4, 5, 2]))  # output: 3

# 15. Make every second character uppercase
def every_second_upper(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

print(every_second_upper("hello"))  # output: HeLlO

# 16. Square each number in a list
def square_list(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

print(square_list([3, 12, 5, 2, 6]))  # output: [9, 144, 25, 4, 36]

# 17. Capitalize every second character in a string
def capitalize_every_second(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

print(capitalize_every_second("hello"))  # output: HeLlO
