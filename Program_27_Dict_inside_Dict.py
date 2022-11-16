#Creating the dictionary and then nesting dictionary inside it.
users = {
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
        'location':'Precenton'
    },
    'mcurie':{
        'first':'marie',
        'last':'currie',
        'location':'paris'
    }    
}
for user_name, user_info in users.items():
    print(f"The Username is {user_name}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\t", full_name.title(),location.title())