import pickle
###Pickling is used to store the obj state or u can say obj data in a file in binary format(serialization)
###Unpickling is used to get the obj state from file in binary(Deserialization)

class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)


with open("emp.dat","wb") as f:
    e=Employee(100,'Durga',1000,'Hyd')
    pickle.dump(e,f)
    print("Pickling of Employee Obj Completed")

with open("emp.dat", "rb") as f:
    obj=pickle.load(f)    
    print("Employee Info After Unpickling...")
    obj.display() 



customDict = {'name':'vivek','salary':'1000','age':'35'}
with open("dict.dat", "wb") as f:
    pickle.dump(customDict,f)
    print("Pickling of Dictionary Completed...")

with open("dict.dat", "rb") as f:
    dictObj=pickle.load(f)
    print(type(dictObj))
    #<class 'dict'>   so dictObj is the refrence to the dict class object dictObj.
    print("Unpickling of Dictionary Completed")
    print(dictObj)      