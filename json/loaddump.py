import json

##json string to dictonary json.loads()

##person is a json string
person = '{"name": "Vivek Singh","age":"30","languages": ["English", "Hindi"]}'
json_dict = json.loads(person)

print(json_dict["age"])
print(json_dict)
print(json_dict["languages"])

###Read Json File##########
##json.load() loads file and convert to 

with open("D:\gitRepo\Python_Code\json\data.json") as f:
    data=json.load(f)

    print(data)
    
    print(type(data))
    #<class 'dict'>
    print(data['quiz']['sport']['q1']['question'])
    print(data['quiz']['sport']['q1'])

    '''
    {'quiz': {'sport': {'q1': {'question': 'Which one is correct team name in NBA?', 'options': ['New York Bulls', 'Los Angeles Kings', 'Golden State Warriros', 'Huston Rocket'], 'answer': 'Huston Rocket'}}, 'maths': {'q1': {'question': '5 + 7 = ?', 'options': ['10', '11', '12', '13'], 'answer': '12'}, 'q2': {'question': '12 - 8 = ?', 'options': ['1', '2', '3', '4'], 'answer': '4'}}}}
<class 'dict'>
Which one is correct team name in NBA?

'''
    print(data['quiz']['sport']['q1']['options'][2])
     


    '''
    for keys,values in data.items():
        print ("keys are {},  values are {}".format(keys,values))

        '''








 ###Python dictionary to string json.dumps()   
 
    dictperson = {"name": "Vivek Singh","age":"30","languages": ["English", "Hindi"]}
    print(type(dictperson))
     
    print(type(json.dumps(dictperson)))
    print(json.dumps(dictperson))


    """
    All the objects in python and their equivalent conversion to json can only occur oif they are
    dict
    list
    tuple
    strin
    int
    float
    Bool
    None

    """