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


# fruits = ['orange', 'Apple', 'Banana', 'Guava', 'kiwi', 'Pomogranate']
# # print(fruits.count("Apple"))

# # fruits.sort()  #this will sort the list in the ascending order

# fruits.reverse()  #this will rreverse the list
# print(fruits)

# fruits.clear()  #this will clear all the list
# print(fruits)





''' 
    Slicing List...
 '''

number = [1,2,3,4,5,6,7,8,9]
# print(number[2:5])  #3,4,5
# print(number[:5])   #1,2,3,4,5
# print(number[2:])   #3,4,5,6,7,8,9
# print(number[-2:])  #8,9
# print(number[::2])   #jump 2 steps
# print(number[::-1])   #print from reverse



# for index,num in enumerate(number):
#     print(index,num)


# lst = []

# for x in range(10):
#     lst.append(x**2)

# print(lst)

# num = [x**2 for x in range(10)]
# print(num)



''' 
    list comprehension with conditions
'''

# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)

# print(lst)

# even_number = [num for num in range(10) if num % 2 == 0]
# print(even_number)


''' 
    Nested list comprehension
'''

# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]

# pair = [[i, j] for i in list1 for j in list2]
# print(pair)



''' 
    list comprehension with function calls
'''

words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)