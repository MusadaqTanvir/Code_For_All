#creating the dictionary
people = {
    'jeny':'C',
    'philip':'Python',
    'Sarah':'C++',
    'edward':'Java',
}
#to check sarah's favourite language 
language = people['Sarah'].title()
print(f"Sarah's favourite language is {language}")

#Using Get() method to reterieve values from the dictionaries...
Language2 = people.get('philip','No such key exists')
print(Language2)