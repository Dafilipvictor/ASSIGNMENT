class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Teacher(Student):
  def __init__(self, firstname, lastname, age, rank): 
    super().__init__(firstname, lastname, age)
    self.rank = rank

teacher_1 = Teacher("Paul", "Aaron", 40, 14)
teacher_2 = Teacher("Dashan", "Peter", 35, 10)

print(teacher_1.firstname)
print(teacher_2.age)



