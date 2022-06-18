# key : value

def displayDict(d):
    for i in d:
        print(d[i])

# days = {}
# print(type(days))
# no repetation
days = {'day1': 'Sunday', 'day2':'Monday', 'day3':'Tuesday' }
displayDict(days)
# print('After adding new day')
days['day4'] = 'Wednesday'
# displayDict(days)
# print('After adding wrong day')
# days['day4'] = 'Wrongday'
# displayDict(days)
# print('After removing wrong day')
# days.pop('day4')
# displayDict(days)

# Display only values
print(days.values())
# Display only keys
print(days.keys())
# display total number of element
print(len(days))

#check sunday is present in dict
print('Sunday' in days.values())

#check day2 is present in dict
print('day2' in days)

for i,j in zip(days.keys(),days.values()):
    print(i,'is',j)