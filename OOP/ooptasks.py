# Create a class to represent a car, with attributes for make, model, year, and current speed. The class should have methods for accelerating and braking. 
"""
class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        pass

    def description(self):
        return f"{self.make, self.model, self.year,} The current speed is {self.speed}"
    
    def braking(self):
        return self.speed
    
    def accelerating(self):
        return self.speed

if __name__ == "__main__":
    myHonda = Car("Honda", "Jazz Sport", "2008", 12)
    print(myHonda.description)
"""

#Create a class to represent a bank account, with attributes for the account holder's name and balance. The class should have methods for deposit, withdraw, and checking the balance. 
"""
class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        pass

    def details(self):
        return f"{self.name} has a balance of ${self.balance}"

    def check_bal(self):
        print(f"You have a balance of ${self.balance}")
        return self.balance
    
    def deposit(self):
        user_input = int(input("How much would you like to deposit?:    "))
        self.balance += user_input
        return self.balance
    
    def withdraw(self):
        user_input = int(input("How much would you like to withdraw?:   "))
        self.balance -= user_input
        return self.balance
if __name__ == "__main__":
    JamalAccount = Bank_account("Jamal", 0)
    print(JamalAccount.details())
    JamalAccount.check_bal()
    JamalAccount.deposit()
    JamalAccount.withdraw()
"""

# Create a class to represent a rectangle, with attributes for width and height. The class should have methods for calculating the area and perimeter. 
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def description(self):
        print(f"Rectangle with a width of {self.width} and a height of {self.height}")
        return self.width, self.height
    
    def area_calc(self):
        area = self.width * self.height
        print(f"Your Rectange has an area of {area} units^2")
        return area
        
    def perimeter_calc(self):
        perimeter = 2*self.width + 2*self.height
        print(f"Your Rectange has a perimeter of {perimeter}")
        return perimeter

if __name__ == "__main__":
    myRec = Rectangle(10, 10)
    myRec.description()
    myRec.area_calc()
    myRec.perimeter_calc()
"""

#Create a class to represent a person, with attributes for first name, last name, and date of birth. The class should have methods for calculating the person's age. 
"""
class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        pass
    def age_calc(self):
        age = 2026 - self.dob
        print(f"You are {age} years old")
        return age
    
if __name__ == "__main__":
    myPerson = Person("Elvin", "Aghdassi", 2008)
    myPerson.age_calc()

"""
    
#Create a class to represent a library, with attributes for books and users. The class should have methods for checking out books, returning books, and keeping track of which books are currently checked out. 

class Library:
    def __init__(self, books, users):
        self.books = books
        self.users = users
        pass
    def track_book(self): 
        print(f"{self.users} has checked out")
        for books in self.books: 
            print(books)
        return self.books
    
    def return_books(self):
        print(f"\n{self.users}'s Books are")
        for books in self.books:
            print(books)
        user_input = input(str("Which book would you like to return?    "))
        self.books.append(user_input)
        return self.books
    
    def checkout_book(self):
        print(f"\n{self.users} checked out books are:")
        for books in self.books:
            print(books)
        user_input = input(str("Which book would you like to checkout?:   "))
        self.books.remove(user_input)
        print(f"\n{self.users} checked out books are now:")
        for books in self.books:
            print(books)
        return self.books
    
if __name__ == "__main__":
    myBooks = Library(["Tu", "1984", "Animal Farm"], "Elvin")
    myBooks.track_book()
    myBooks.return_books()
    myBooks.checkout_book()

