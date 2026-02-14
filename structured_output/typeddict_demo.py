from typing import TypedDict

class Person(TypedDict):
    name: str 
    age: int 

new_person: Person = {'name':'haseeb', 'age': 30} #'30'

print(new_person)