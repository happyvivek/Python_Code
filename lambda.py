#Lambda functions which doesnt have name 
#They are exclusively used to operate on sinputs and return the outputs.
#They are never used to perform actions

def add(x, y):
    return x + y

print(add(2,4))    


add = lambda x, y : x + y

print(add(1,2))

#Not Common
print((lambda x, y : x + y)(5,7))

#Useful Usage

def double(x):
    return x*2
sequence = [1, 3, 5, 6, 7, 8]
double = [double(element) for element in sequence]
print(double)

#Instead of above list comprehension use map,thats where lambda functions excel
doubled = map(double, sequence)

#Rewrite using lambda

double = [ (lambda x:x*2)(element) for element in sequence]

print(double)

#Best way is to use map

doubled = list(map(lambda x:x*2,sequence))
print(doubled)