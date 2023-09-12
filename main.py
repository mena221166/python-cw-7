class person :
    name = 'mena'
    age = 17
    
    def is_adult():
     if person.age >= 18:
      print("you have too much responsibilit ")
     else:
       print(" lucky you ")
       
print(person.name)
print(person.age)
person.is_adult()


class person1:
   def __init__(self, name, age):
      self.name =name
      self.age =age
   def __str__(self):
      return f"my name is {self.name} and uam {self.age} years old"
   
first_person= person("manal",22)
print(first_person)