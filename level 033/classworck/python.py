def manual_transform(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

squared_numbers = manual_transform(square, numbers)
print("Squared:", squared_numbers)  # [1, 4, 9, 16, 25]





def manual_filter(predicate, iterable):
    result = []
    for item in iterable:
        if predicate(item):
            result.append(item)
    return result

names = ["Ryan", "Kieran", "Jason", "Yous"]
filtered_names = manual_filter(lambda x: len(x) == 4, names)
print(filtered_names)  # Output: ["Ryan", "Yous"]
