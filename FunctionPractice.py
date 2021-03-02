import math
def comapareNum(num1,num2):
    if(num1 == num2):
        return True
    else:
        return False

input1 = int(input("Enter first number :"))
input2 = int(input("Enter Second number :"))
StringIn = input("Enter a String :")

result = comapareNum(input1,input2)
power = math.pow(input1,input2)

print(power)

if(result):
    print("Both are same")

else:
    print("Both are different")

print(StringIn.capitalize())
