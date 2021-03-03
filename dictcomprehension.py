#Mapping of Username to username Info
users = [
    ("vivek",30,1000,"M"),
    ("Ram",40,1000,"M"),
    ("Laxmi",50,"F")
    ]

##Created mapping of username with associated tuple as dictionary
username_mapping = {user[0]:user for user in users}

print(username_mapping)
print(type(username_mapping))

###How is this usefu
###You know the username and waht to get full info about thim

print(username_mapping["Laxmi"])

