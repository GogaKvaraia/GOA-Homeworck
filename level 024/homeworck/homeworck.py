print("=== List Operations ===")
my_list = [1, 2, 3]

my_list.append(4)
print("After adding 4:", my_list)

my_list.insert(1, 'a')
print("After inserting 'a':", my_list)

my_list.remove(2)
print("After removing 2:", my_list)

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping:", my_list)

print("First element:", my_list[0])
print("Length of list:", len(my_list))

my_list.extend([5, 6])
print("After extending:", my_list)

my_list.reverse()
print("After reversing:", my_list)

my_list.sort()
print("After sorting:", my_list)

sliced_list = my_list[1:4]
print("Sliced list:", sliced_list)






print("\n=== Tuple Operations ===")
my_tuple = (1, 2, 3)

print("First element:", my_tuple[0])
print("Length of tuple:", len(my_tuple))

tuple_to_list = list(my_tuple)
print("Converted tuple to list:", tuple_to_list)

try:
    my_tuple[0] = 5
except TypeError as e:
    print("Error:", e)







print("\n=== Set Operations ===")
my_set = {1, 2, 3}

my_set.add(4)
print("After adding 4:", my_set)

my_set.remove(2)
print("After removing 2:", my_set)

print("Is 3 in the set?", 3 in my_set)
print("Length of set:", len(my_set))

another_set = {3, 4, 5}

intersection = my_set.intersection(another_set)
print("Intersection:", intersection)

union = my_set.union(another_set)
print("Union:", union)

difference = my_set.difference(another_set)
print("Difference:", difference)

my_set.clear()
print("After clearing the set:", my_set)
