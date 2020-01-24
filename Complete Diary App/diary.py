#!/usr/bin/env python3

#python libraries
from collections import OrderedDict
import datetime
import os
import sys

#third party libraries
from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
  
    class Meta:
        database = db
        
def initialize():
  """Create the database and the table if they don't exist."""
  db.connect
  db.create_tables([Entry], safe=True)
  
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#then we run through menu. Set the choice to none by default. While choice is not quitting we clear (clean interface) and then loop through our menu choices (ordered dict) one by one. We then let the user input their choice. If the choice is in the menu we clear (clean interface) and then we run the function connected the the entered value (as defined in our ordered dictionary).    
def menu_loop():
    """show the menu"""
    choice = None
    
    while choice != 'q':
      clear()
      print("Enter 'q' to quit.")
      for key, value in menu.items():
        print('{}) {}'.format(key, value.__doc__))
      choice = input('Action: ').lower().strip()
      
      if choice in menu:
          clear()
          menu[choice]()
  
def add_entry():
    """add an entry"""
    print("Enter your entry. Press ctrl + d when finished")
    data = sys.stdin.read().strip()
    
    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content=data) 
            print("Saved successfully!")

  
#our main function. We select entries, clear interface then if there is a search query we create a variable of entries that are composed of our search query returns. If not we loop straight through our compilation of entries, printing their time stamp, a break using '=' with no of = through character number, the entry content then set two break lines and options for the user.

#if q, we break. If d we run the delete entry function. If (although not defined as our for loops runs it regardless on character != dq) any other character it will go to next entry.
def view_entries(search_query=None):
    """view previous entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    clear()
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    
    for entry in entries:
      timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
      print(timestamp)
      print('='*len(timestamp))
      print(entry.content)
      print('\n\n' + '='*len(timestamp))
      print('n) next entry')
      print('q) return to main menu')
      print('d) delete entry')
      
      next_action = input('Action: [Nq] ') .lower().strip()
      if next_action == 'q':
        break
      elif next_action == 'd':
        delete_entry(entry)
  
def search_entries():  
    """Search entries for a string"""
    view_entries(input('Search query: '))

def delete_entry(entry):
    """delete an entry"""
    if input("Are you sure [yN] ").lower() == 'y':
      entry.delete_instance()
    
#defining an ordered dictionary of key value pairs - values and functions. Once user enters value, function is called through accessing the ordered dict.
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])
  
#before running any code python sets a few variables. It sets __name__ to __main__. So what we are saying here is that if __name__ is equivalent to __main__  we will run the initialize function (creating an instance of the database and table if they don't exist) and loop through our menu. We are giving a beginning clause when the program runs?
if __name__ == '__main__':
    initialize()
    menu_loop()