print("Anisha")
print(" Pandey")
a = input("Enter yur name here: ")
print (a)
#sum of two number 
a = int(input("Enter value of first number:"))
b = int(input("Enter value of second number:"))
sum = a+b
print (sum)
# aVERAGE OF two number 
average =float((a+b)/2)
print(average)

# conditional statement
color = input("Enter yur color :")
 
if color == "red":
    print("Please stop!!")
elif color == "green":
    print("Time to go!!")
elif color == "yellow":
    print("Time to ready!!!")    
else:
    print("You choose wrong color for traffic light")        
# check user name and password
username = input("Enter user name: ") 
password =input("Enter password :")
if (username=="admin" and password =="12345"):
  print("Login Successfully")
elif (username!="admin"):
    print("Wrong userID")
else:
    print("Wrong Password")   
# check number is even or odd 
a = int(input(" Enter yur number:")) 
if a%2==0:
  print("Number is even")
else:
    print("Number is odd")
# Write a program using match case prblm
color = input("Enter color of traffic light: ")
match color:
    case "Green":
       print("GO")
    case "Yellow":
        print("LOOK")
    case "RED":
        print("STOP!!")
    case _:
        print("Wrong color")   
# multiplication of number 
num = int(input("Enter yur table number: "))
count = 1
while(count<=10):
    print(num,"X",count," = ",num*count)
    count+=1
print("Value of count: ", count)



