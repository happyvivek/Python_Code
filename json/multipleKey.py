import json

list1 = ['data["quiz"]["sport"]','data["quiz"]["sport"]["q1"]','data["quiz"]["sport"]["q1"]']

for elements in list1:

    with open('D:\gitRepo\Python_Code\json\data.json') as f:
        data = json.load(f)
        print(type(data))
        element=elements.replace('\"','\'')
        print(element)
        
    
