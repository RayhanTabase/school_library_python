class Classroom:
  def __init__(self, label):
    self.__label = label
    self.__students = []
  
  @property
  def label(self):
    return self.__label 
  
  @label.setter
  def label(self, label):
    self.__label = label
    
  def add_student(self, student):
    if not student in self.student:
      self.__students.append(student)
      
    if not student.classroom == self:
      self.classroom = self
      