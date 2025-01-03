#ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის
# დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
# დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
# დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
# კომენტარებით ახსენით რაში გვადგება try/except




#2

try:
    print(a)
except NameError:
    print("Variable 'a' is not defined.")





#3


try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index is out of range.")





#4


try:
    num = int("abc")
except ValueError:
    print("Cannot convert string to integer.")

