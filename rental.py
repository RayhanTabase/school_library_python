class Rental:
  def __init__(self, person, book, date):
      self.__person = person
      self.__book = book
      self.__date = date
      person.add_rental(self)
      book.add_rental(self)
      
  @property
  def person(self):
    return self.__person
  
  @property
  def book(self):
    return self.__book 
  
  @property
  def date(self):
    return self.__date 