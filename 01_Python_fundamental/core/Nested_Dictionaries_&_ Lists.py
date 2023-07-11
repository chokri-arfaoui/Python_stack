# 1/Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# x[1][0]=15
# print(x)



# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name']='Bryant'
# print(students)


# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0]='Andres'
# print(sports_directory)


# Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y']=30
# print(z)


# 2/Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'}, 
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# for i in range(4):
#     print (  students[i]['first_name']  ,   students[i]['last_name'])


# iterateDictionary2('first_name', students)
# for i in range(4) :
#     print(students[i]['first_name'])    


# iterateDictionary2('last_name', students) 
# for i in range(4):
#     print(students[i]['last_name'])



# Iterate Through a Dictionary with List Values

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# for i in range(7):
#     print (dojo['locations'][i])


for i in range(8):
    print (dojo['instructors'][i])