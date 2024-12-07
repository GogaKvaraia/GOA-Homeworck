def calculate_sum(numbers):
    return sum([int(num) if isinstance(num, int) else int(num) if num.isdigit() else 0 for num in numbers])

numbers = [10, "10", "5", 5, "abc", 20]
result = calculate_sum(numbers)
print(result)
