'''
# the_count = [1,2,3,4,5]
chesburger_ingridiends = ["cheeeeeese", "cows", "socks", "says-uh-me seed bun", "cheeps"]
print (chesburger_ingridiends[3])
# print (len(the_count))
# for dragon_of_nonexistence in the_count:
#     print (dragon_of_nonexistence*2)
length = len(chesburger_ingridiends)
range (3)
range(len(chesburger_ingridiends))
for num in range(len(chesburger_ingridiends)):
    item =chesburger_ingridiends
strOne = "hello world!"
listOne = list(strOne)
print(listOne)
listOne[11] = '.'
print(listOne)
# adding stuff 2 list
chesburger_ingridiends.append("flies,")
print(chesburger_ingridiends)
# list of letters the player has guessed
chesburger_ingridiends.pop(1)
print(chesburger_ingridiends)
chesburger_ingridiends.remove("socks")
print(chesburger_ingridiends)
# # abcs
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# #  make da lowercase
# strTwo = "THis is A verY OdD sEnTencE"
# lowercase =strTwo.lower()
# print(lowercase)
.join

#dictionaries-key: value pair
dictionary = {"name": 'Lance', 'age': 1000, 'height': 0}
#accessing things from dictionary.
print(dictionary["name"])
print(dictionary['age'])
print(dictionary['height'])
dictionary['profession'] = 'telemarketer'

large_dictionary = {
    'ca': 'california',
    'az': 'arizona',
    'ny': 'new yorkshire'
}
print(large_dictionary['ny'])
larger_dictionary = {
    'ca': 'fresno',
}

large_dictionary = {
    'ca': 'california',
    'az': 'arizona',
    'ny': 'new yorkshire'
}
largest_dictionary = {
    'ca': {
        'name': 'california',
        'population': '39250000',
        'border st': [
            'oregon',
            'nevada',
            'arizona',
        ]
    },
    'az': {},
    'ny': {}
}
current_node = largest_dictionary['ca']
#print(current_node['border st'][1])
'''
