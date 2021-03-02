import json

##jsonDecode Exception
incorrect_json = '{ name":"John "age":30 "car:"None" }'
try:
	a_json = json.loads(incorrect_json)
	print(a_json)
except json.decoder.JSONDecodeError:
	print("String could not be converted to JSON")



correct_json = '{"name":"John","age":30,"car":"None" }'

try:
    a_json=json.loads(correct_json)
    print(a_json)
    print("correct json found")
except json.decoder.JSONDecodeError:
    print("correctjson not found")    


##KeyError exception handling

with open('D:\gitRepo\Python_Code\json\data.json') as f:
    try:
        data = json.load(f)
        print(data)
        print("***************LINE************")
        ###keyError will be handled by data.get() as it returns None if key not found
        ###In case of (key).[0] if key doesnt exist
        ##print(data.get('quiz').get('sport').get('q1').get('option1')[0])
         #####TypeError: 'NoneType' object is not subscriptable
        ##The best way is to create function and pass key as arguments
        # If key Error return None: 
        print(data.get('quiz').get('sport').get('q1').get('options')[0])
    except json.decoder.JSONDecodeError:    
        print("Error in json Decoding")

try:
    print(data['quiz']['sport1'])
except KeyError:
    print("keyError Encountered")

