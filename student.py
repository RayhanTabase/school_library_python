
from person import Person
class Student(Person):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__classroom = None
        
  def play_hooky(self):
    return '¯\(ツ)/¯'
  
  @property
  def classroom(self):
    return self.__classroom
  
  @classroom.setter
  def classroom(self, classroom):
    self.__classroom = classroom
    classroom.add_student(self)
  