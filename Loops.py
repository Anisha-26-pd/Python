#Give me the example of break and continue statement
i =1
while(i<=10):
    if(i%6==0):
        break
    print(i)
    i+=1
    
# continue statement
print("continue statement begin here")
j=1
while(j<=10):
    if(j%3==0):
        j+=1
        continue
    print(j)
    j+=1
print("break next program start")
# use for loop and in operator
string ="Anisha Pandey"
for ver in string:
    print(ver) 
# Print count of vowel in word intelligence
word = "intelligence"
count =0
for ch in word:
  if (ch =="a" or ch =="e" or ch =="i" or ch =="o" or ch =="u"):
     count+=1
print("Number of vowels in given word is :", count)
# print sum of n number
n = int(input("Enter yur number for sum: "))
sum = 0
for i in range( n+1):
    sum+=i
print(sum)