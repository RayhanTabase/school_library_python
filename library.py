from inputs import Inputs
from student import Student
from teacher import Teacher
from rental import Rental
from book import Book

class Library:
  def __init__(self):
    self.__books = []
    self.__people = []
    self.__rentals = []
    
  def list_all_books(self):
    count = 1
    for book in self.__books:
      print(f"{count}) Title: {book.title}, Author: {book.author}")
      count += 1
      
  def list_all_people(self):
    count = 1
    for person in self.__people:
      print(f"{count}) Name: {person.name}, ID: {person.id}, Age: {person.age}")
      count += 1
      
  def list_rentals_for_id(self, id):
    for rental in self.__rentals:
      if rental.person.id == id:
        print(f"Date: {rental.date} , Book: {rental.book.title} by {rental.book.author}")
        
  def __create_student(self):
    age = Inputs.input_number_range('Age', int, 5 , 100)
    name = Inputs.input_string_alphabets('Name', 2, 200)
    has_parental_permission = Inputs.input_bool('Has parent permission?')
    new_person = Student(age, name, has_parental_permission)
    self.__people.append(new_person)
    
    
  def __create_teacher(self):
    age = Inputs.input_number_range('Age', int, 5 , 100)
    name = Inputs.input_string_alphabets('Name', 2, 200)
    specialization = Inputs.input_string_alphabets('Specialization', 2, 200)
    new_person = Teacher(specialization, age, name)
    self.__people.append(new_person)
    
    
  def create_person(self):
    print('Do you want to create a student(1) or a teacher(2)?')
    option = Inputs.input_number_range('Input the number',int,1,2)
    if option == 1:
      self.__create_student()
    else:
      self.__create_teacher()
    print('Person created successfully')
    
  
  def create_book(self):
    title = Inputs.input_string('Title', 1, 300)
    author = Inputs.input_string_alphabets('Author', 1, 200)
    new_book = Book(title, author)
    print('Book created successfully')
    self.__books.append(new_book)
    
  def create_rental(self):
    if len(self.__books) == 0:
      print('No books available')
      return
    if len(self.__people) == 0:
      print('No person available')
      return
    print('Select a book from the following list of numbers')
    self.list_all_books()
    book_index = Inputs.input_number_range(1, len(self.__books))
    book = self.__books[book_index]
    print('Select a person from the following list of numbers (not_id)')
    self.list_all_people()
    person_index = Inputs.input_number_range(1, len(self.__people))
    person = self.__people[person_index]
    date = Inputs.input_string('Date', 4, 30)
    new_rental = Rental(person, book, date)
    print('Rental created successfully')
    self.__rentals.append(new_rental)
    
  def display_menu(self):
    options = [
      'List all books',
      'List all people',
      'Create a person',
      'Create a book',
      'Create a rental',
      'List all rentals for a given person id',
      'Exit'
    ]
    
    print('Please choose an option by entering a valid number: ')
    print(' ')
    count = 1
    for option in options:
      print(f"{count} - {option}")
      count += 1

  def display_sub_menu(self,option):
    if option == 1:
      self.list_all_books()
    elif option == 2:
      self.list_all_people()
    elif option == 3:
      self.create_person()
    elif option == 4:
      self.create_book()
    elif option == 5:
      self.create_rental()
    elif option == 6:
      self.list_rentals_for_id()
      