
numbers = [2, 4, 6, 8, 10]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

names = ["Alice", "Bob", "Charlie"]
greetings = list(map(lambda name: f"Hello, {name}", names))
print(greetings)

words = ["apple", "banana", "kiwi"]
lengths = list(map(len, words))
print(lengths)

numbers = [-5, 3, -2, 7, 0, 10]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)

words = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda word: word.startswith("p"), words))
print(p_words)

numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)
