info =[
      ("Anisha", "Maths"),
      ("Bob", "Science"),
      ("Alice", "English"),
      ("Charlie", "Geography"),
      ("Bob", "Maths"),
      ("Alice", "English"),
      ("Charlie", "Science")
]
#list all unique course
s = set()
m = set()
for tup in info:
    s.add(tup[1])
print(s)
#list students enrolled in English
for name, course in info:
    if(course=="English"):
      m.add(name)
print("Student enrolled in English :", m)
#Create Dictionary (student, set of course)
dic = {}
for name, course in info:
   if(dic.get(name)==None):
      dic.update({name:set()})
      dic[name].add(course) #here they open dictionary list so it uses square bracket with name
   else:
      dic[name].add(course)
print(dic)   
