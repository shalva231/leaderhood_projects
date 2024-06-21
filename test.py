A = int(input("please enter the first side of the triangle: "))
B = int(input("please enter the second side of the triangle: "))
C = int(input("please enter the third side of the triangle: "))

if A + B > C:
    if B + C > A:
        if A + C > B:
            print("this is a triangle")
else:
    print("this is not a triangle")