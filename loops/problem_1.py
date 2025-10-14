# for i in range(1, 10, 2):
#     print(i)


# str = "Mobashshir Hasan"

# for i in str:
#     print(i)




"""The While loop continues to execute as long as the condition is True."""

# count = 0
# while count < 10 :
#     print(count)
#     count = count + 1




''' Loop Control Statements'''
# Break 
#  break statement exits the loop permanently

# for i in range(10):
#     if i == 5:
#         break
#     print(i)





''' 
Continue :
The continue statement skips the current iteration and continues with the next.  
'''

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)




''' 
Pass : The pass statement is null operation, and does nothing
'''

for i in range(5):
    if i == 3:
        pass
    print(i)