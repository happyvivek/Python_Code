
#List comprehensions List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

namelist = ["vivek","pingh","pavish","pm","am"]
namelist1 = ["vivek","pingh","pavish","pm","am"]

numbers = [1,2,3,4,5,6]

namelist= [name for name in namelist if "pm" == name]
print(namelist)
newlist = [name for name in namelist1 if name.startswith("p")]
print(newlist)
    
newnumlist = [x*2 for x in numbers]
print (newnumlist)

 
######If you dont use list comprehension last code will look like this############

for y in numbers:

     newnumlist.append(y*2)
     print(newnumlist)

for name in namelist:
    if "pm" == name:
        newlist.append(name)
        print(newlist)
 