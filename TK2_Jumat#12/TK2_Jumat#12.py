# Function 1 = Constant 0
def function_1(x,y):
    return 0

#Function 2 = AND = z = x.y
def function_2(x,y):
    return 1 if (x == 1 and y == 1) else 0

#Function 3 = z = x.!y
def function_3(x,y):
    return (x and int(not y))

#Function 4 = z = x
def function_4(x,y):
    return x

#Function 5 = z = !x.y
def function_5(x,y):
    return (int(not x) and y)

#Function 6 = z = y
def function_6(x,y):
    return y

#Function 7 = XOR = !x.y+x.!y
def function_7(x,y):
    return ((int(not x)and y)or(x and int(not y)))

#Function 8 = OR = z = x + y
def function_8(x,y):
    return (x or y)

#Function 9 = NOR = z = !(x+y)
def function_9(x,y):
    return int(not(x or y))

#Function 10 = XNOR = xy + !x.!y
def function_10(x,y):
    return ((x and y) or (int(not x) and int(not y)))

#Function 11 = z = !y
def function_11(x,y):
    return int(not y)

#Function 12 =  z = x + !y
def function_12(x,y):
    return (x or int(not y))

#Function 13 = z = !x
def function_13(x,y):
    return int(not x)

#Function 14 = IMPLICATION = z = !x + y
def function_14(x,y):
    return (int(not x) or y)

#Function 15 = NAND = z = !(x.y)
def function_15(x,y):
    return (int(not(x and y)))

#Function 16 = Constant 1
def function_16(x,y):
    return 1

#Main program
while 0 != 1:
    print("Piliha operasi fungsi boolean :")
    print("Function 1 : Constant 0")
    print("Function 2 : x.y")
    print("Function 3 : x.!y")
    print("Function 4 : x")
    print("Function 5 : !x.y")
    print("Function 6 : y")
    print("Function 7 : !x.y+x.!y XOR")
    print("Function 8 : x + y (OR)")
    print("Function 9 :!(x+y) (NOR")
    print("Function 10 : xy+!x!y (XNOR")
    print("Function 11 : !y")
    print("Function 12 : x+!y")
    print("Function 13 : !x")
    print("Function 14 : !x+y (IMPLICATION")
    print("Function 15 : !(x.y) (NAND)")
    print("Function 16 : Constant 1") 
    print("Masukkan fungsi yang diinginkan : ")
    inputUser = int(input())
    print("\n")
    if inputUser == 1:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_1(x,y)))
    elif inputUser == 2:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_2(x,y)))
    elif inputUser == 3:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_3(x,y)))
    elif inputUser == 4:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_4(x,y)))
    elif inputUser == 5:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_5(x,y)))
    elif inputUser == 6:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_6(x,y)))
    elif inputUser == 7:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_7(x,y)))
    elif inputUser == 8:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_8(x,y)))
    elif inputUser == 9:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_9(x,y)))
    elif inputUser == 10:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_10(x,y)))
    elif inputUser == 11:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_11(x,y)))
    elif inputUser == 12:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_12(x,y)))
    elif inputUser == 13:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_13(x,y)))
    elif inputUser == 14:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_14(x,y)))
    elif inputUser == 15:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_15(x,y)))
    elif inputUser == 16:
        print("x y z")
        for x in (0, 1) :
            for y in (0, 1) :
                print(str(x) + " " + str(y) + " " + str(function_16(x,y)))
    else:
        print("The function is not availible")
    print("\n")