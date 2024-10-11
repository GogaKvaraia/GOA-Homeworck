def manual_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def manual_min(lst):
    if not lst:
        return None  # Handle empty list case
    minimum = lst[0]
    for item in lst:
        if item < minimum:
            minimum = item
    return minimum

# Example test cases
print(manual_sum([1, 2, 3, 4]))  # 10
print(manual_len([1, 2, 3, 4]))  # 4
print(manual_min([3, 1, 4, 2]))  # 1
