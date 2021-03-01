num1 = int(input("Enter A number:"))
num2 = int(input("Enter Last Number:"))
num3 = range(num1,num2)

for index,number in enumerate(num3,start = 1):
  if number == 0:
   print("U started wtih zero")

  else:
   print(index,'#',number)
