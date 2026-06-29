from enum import Enum

class Person:
    _count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person._count += 1

    def introduction(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
    
    @classmethod
    def get_count(cls):
        return cls._count
    
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduction(self):
        print (f"Hi, I'm {self.name} and I'm {self.age} years old. I'm a {self.major} student")
    
class Role(Enum):
    PROFESSOR = "Professor"
    LECTURER = "Lecturer"
    ASSISTANT = "Assistant"

class Lecturer(Person):
    def __init__(self, name, age, role: Role):
        super().__init__(name, age)
        self.role = role

    def introduction(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old. I'm a {self.role.value}")