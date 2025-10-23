num = int(input("Enter a number : "))   #5

for i in range(1, num+1):  #row
    for j in range(1, num+1):  #column
        # print("* ", end= " ")
        if i == 1 or i == num:
            print("*", end=" ")
        else:
            if j == 1 :
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print("\n")