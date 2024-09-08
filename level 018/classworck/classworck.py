text = "hello"
result = text.upper()  # აქ "hello" გადაიქცევა "HELLO"-ში
print(result)  

text = "HELLO"
result = text.lower()  # აქ "HELLO" გადაიქცევა "hello"-ში
print(result)  

text = "hello world"
result = text.capitalize()  # აქ "hello world" გადაიქცევა "Hello world"-ში
print(result)  

text = "Hello World"
result = text.swapcase()  # აქ "Hello World" გადაიქცევა "hELLO wORLD"-ში
print(result)  

text = "hello world"
position = text.find("world")  # "world" იწყება ინდექსზე 6
print(position)  

text = "hello"
length = len(text)  # "hello" სიგრძე არის 5
print(length)  

text = "hello world"
position = text.index("world")  # "world" იწყება ინდექსზე 6
print(position)  

my_list = [1, 2, 3]
my_list.append(4)  # დაამატებს 4-ს სიას
print(my_list)  

my_list = [1, 2, 3]
my_list.insert(1, 'a')  # დაამატებს 'a'-ს ინდექსზე 1
print(my_list) 

my_list = [1, 2, 3]
popped_element = my_list.pop()  # ამოიყვანს და აბრუნებს ბოლო ელემენტს (3)
print(popped_element) 
print(my_list)  

my_list = [1, 2, 3]
my_list.remove(2)  # ამოიყვანს პირველი გაწვდას ელემენტს 2
print(my_list) 





