class Book:
  def __init__(self,title, author):
    self.__title = title
    self.__author = author
    self.__rentals = []
    
  def add_rental(self, rental):
    self.rentals.append(rental)
  
  @property
  def title(self):
    return self.__title
  
  @property
  def author(self):
    return self.__author
  
  @property
  def rentals(self):
    return self.__rentals
  
  def add_rentals(self, rental):
    self.__rentals.push(rental)