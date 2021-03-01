num1 = int(input("Enter A number:"))
num2 = int(input("Enter Last Number:"))
num3 = range(num1,num2)

for index,number in enumerate(num3,start = 1):
  print("testing for loop")
  if number == 0:
   print("U started wtih zero")

  else:
   print(index,'#',number)

while (num1<num2):
    print("now its to test while")
    print("reaching num2 slowly ",num1)
    num1 = num1 +1
