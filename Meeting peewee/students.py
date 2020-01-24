from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    #CharField (or VarChar in SQL) is a field that stores characters. We place max characters we want to store and state we want the usernames to be unique.
    username = CharField(max_length=255, unique=True)
    #IntegerField is a field that stores.. integers. If we don't supply points, set the default to 0.
    points= IntegerField(default=0)
    
    #In peewee and Django you can have classes inside of classes...We can use the meta class to define lots of things.
    class Meta:
        database = db
        
        
students = [
  {'username': 'jamesstirrat',
   'points': 420},
  {'username': 'meganstirrat',
   'points': 421},
  {'username': 'heatherdobbin',
   'points': 422},
  {'username': 'ruthstirrat',
   'points': 423},
  {'username': 'dougstirrat',
   'points': 424},
]


def add_students():
  for student in students:
    try:
        Student.create(username=student['username'],
                  points=student['points']) 
    except IntegrityError:
        student_record = Student.get(username=student['username'])
        if student_record.points != student['points']:
          student_record.points = student['points']
          student_record.save()
   
  
def top_student():
  student = Student.select().order_by(Student.points.desc()).get()
  return student
  
    #if file run directly and not imported. Connect to database and create table for Student Model. safe keyword means that if the database and table already created, peewee won't freak out. It will just move on.
if __name__ == '__main__':
  db.connect()
  db.create_tables([Student], safe=True)
  add_students()
  print("Our top student is: {0.username}.".format(top_student()))
        
    #.create() adds new record to table
    #.select() picks records out of table for us to use
    #.save() will update existing row in the database
    #.get() will fetch a single record from the database
    #.delete_instance() will delete single record from the database
    #.order_by() will set out how the database is ordered
    
    
    
