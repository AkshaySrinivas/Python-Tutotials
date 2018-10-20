# myFile = open("myFile.txt","w")
# myFile.write("Hello World! , Data Written")
# print("Data Written")
# myFile.close

num1 = input("Enter 1st Number : ")
num2 = input("Enter 2nd Number : ")
res = int(num1)+int(num2)
print(res)

myFile = open("myFile.txt","a")
myFile.write(' '+str(res))
print("Data Written")
myFile.close