import random

from corrector import Corrector

class Person:
  def __init__(self, age, name='Unknown', parent_permission=True):
      self.__id = random.randint(1, 10)
      self.__name = name
      self.__age = age
      self.__parent_permission = parent_permission
      self.corrector = Corrector()
      self.__rentals = []
      
  def __is_of_age(self):
    return self.__age >= 18
  
  def can_use_services(self):
    return self.__parent_permission or self.__is_of_age()
  
  @property
  def age(self):
    return self.__age
  
  @property
  def name(self):
    return self.__name
  
  @property
  def id(self):
    return self.__id
  
  @name.setter
  def name(self, name):
    self.__name = name
  
  @age.setter
  def age(self, age):
    self.__age = age
  
  def add_rentals(self, rental):
    self.__rentals.push(rental)
    
    
  def validate_name(self):
    self.__name = self.corrector.correct_name(self.__name)