#normal and old version- format()
print("My name is Anisha Pandey\nmy intro is {}".format("I lived in Delhi"))
a = 12; b = 14
print("sum of {} & {} is {}".format(a,b, a+b))
print("sum of {1} & {0} is {2}".format(a,b, a+b))
#new version- f_string
print(f"average of {a} & {b} is {(a+b)/2}")
# list and method
ani =[23, 45,"hello", 45.90]
ani.append("Anisha")
print(ani)
ani.reverse()
print(ani)
ani.insert(3, "world")
print(ani)
#set
s ={1,2,3,4,5,5}
print(type(s))