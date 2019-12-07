course = {'teacher':'Ashley', 'class':'Introducing Dictionaries', 'level':'Beginner'}

print(course)

#changing our 'teacher' value

course['teacher'] = 'instructor'

print(course)

#changing our 'level' value

course['level'] = 'intermediate'

print(course)

#adding a new key:value pair

course['stage(s)'] = 1

print(course)

#deleting our new entry

del(course['stage(s)'])
    
print(course)

#changing keys

course['leader is'] = course['teacher']
del course['teacher']

print(course)