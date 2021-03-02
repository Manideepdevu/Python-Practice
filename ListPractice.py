totalItem = int(input("Enter Total number of items :"))
index = 1
items1 =[]

while(index<=totalItem):
    if(index == 1):
        items1.append(input("Enter First Value:"))
    elif(index == totalItem):
        items1.append(input("Enter Last Value:"))
    else:
        items1.append(input("Enter Next Value :"))
    
    index = index+1

print("list of items",items1)