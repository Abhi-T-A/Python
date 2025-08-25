#swapping values using 3rd variable

"""num1=10
num2=20
temp=num1
num1=num2
num2=temp
print("After swapping, num1 =", num1, "and num2 =", num2)"""

#using input
num1=int(input("Enter first Number: "))
num2=int(input("Enter second Number:"))

#creating temp variable

print("Before swapping:",num1,num2)
temp=num1
num1=num2
num2=temp
print("After swapping:",num2,num1)

"""
#without using 3rd variable
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

print("Before swapping:", num1, num2)

# swapping without 3rd variable
num1, num2 = num2, num1

print("After swapping:", num1, num2)"""
