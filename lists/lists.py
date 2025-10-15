''' 
    Lists are ordered, mutable collections of item.
    They can contain items of different data types.
'''

# Empty Lists
# lst = []
# print(type(lst))

# names = ["Mobashshir", 'Hasan' , 1, 2, 3, ]
# print(names)

# mixed_lst = [1, "hello", 14.3, True]    # In list we can store any kind of data types
# print(mixed_lst)

''' 
    Accessing Lists[]
'''

# fruits = ['Apple', 'Banana', 'Guava', 'Pomogranate', 'kiwi']
# print(fruits[1:4])
# print(fruits[1:4])


''' 
    Modifying the Lists..
'''

# fruits = ['Apple', 'Banana', 'Guava', 'Pomogranate', 'kiwi']
# fruits[1:] = 'watermelon'
# print(fruits)


''' 
    Lists Method...
'''

# fruits = ['Apple', 'Banana', 'Guava', 'Pomogranate', 'kiwi']
# fruits.append('orange')
# fruits.remove('Apple')
# print(fruits)



# fruits = ['Apple', 'Banana', 'Guava', 'Pomogranate', 'kiwi']
# popped_fruits = fruits.pop()
# print(fruits)


fruits = ['orange', 'Apple', 'Banana', 'Guava', 'kiwi', 'Pomogranate']
# print(fruits.count("Apple"))

fruits.sort()  #this will sort the list in the ascending order
print(fruits)