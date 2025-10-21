# ''' 
#     Prime Number
# '''
# num = int(input("Enter a number :"))

# count = 0 

# for i in range(1, num+1):
#     if num % i == 0:
#         count = count+1

# if count == 2:
#     print("number is prime ")
# else:
#     print("numer is not prime")







# num1 = int(input("Enter number of rows : "))
# # num2 = int(input("Enter number of columns : "))

# for i in range(1, num1+1):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")



# total prime number :
#

# i = 1
# j = 1
# k = 1
# z = 1

# while z <= 5:
#     while i <= 3:
#         print("Mobashshir")
#         i = i + 1
#     while j <= 3:
#         print("Hasan")
#         j = j + 1 
#     while k <= 3:
#         print("Qatar")
#         k = k + 1
#     k = 1
#     j = 1
#     i = 1
#     z = z + 1


num = int(input("Enter a number : "))   #5

for i in range(1, num+1):  #row
    for j in range(1, num+1):  #column
        # print("* ", end= " ")
        if i == 1 or i == num:
            print("*", end=" ")
        else:
            if j == 1 or j == num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print("\n")