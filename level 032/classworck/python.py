numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)


celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 33.8, celsius))
print(fahrenheit)


words = ["hello", "world", "python"]
capitalized_words = list(map(lambda x: x.capitalize(), words))
print(capitalized_words)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)


numbers = [3, 9, 15, 22, 27, 30]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)

