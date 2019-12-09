#def print_teacher(name, job, topic):
    #print(name)
    #print(job)
    #print(topic)

#kwargs allows us more seamless flexibility as we can add more (variable) and grow, without any problems.
def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    
#positional arguments
#print_teacher('Ashley', 'Instructor', 'Python')


#variable arguments - these allow us to identify our variables for us within the function and make our code easier to read and pick up on
print_teacher(name='Ashley', job='Instructor', topic='Python', rating=4)

    
