print("Input values for triangle sides:")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a==b==c:
    print("It is an Equilateral Triangle.")
elif a==b or b==c or c==a:
    print("It is an Isosceles Triangle.")
else:
    print("It is an Scalene Triangle.")
    
