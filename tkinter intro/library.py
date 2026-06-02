import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self):
        self.borrower = None
        self.library_books = ["The Great Gatsby", "Animal Farm","1984","Tu"]
        pass

    def check_out(self, book):
        self.library_books.remove(book)
   
    def return_books(self,book):
        self.library_books.append(book)

class Borrower:
    def __init__(self, name):
        self.name = name
        self.user_books = []
   
    def user_checkout(self, book):
        self.user_books.append(book)

    def user_return(self, book):
        self.user_books.remove(book)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Digital Library")
        self.root.geometry("400x300")

        self.borrower = None

        self.create_frames()
        self.create_widgets()
        self.book_catalogue = Book()

    def create_frames(self):
        self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame = tk.Frame(self.root, padx=10, pady=10)

        self.input_frame.pack(fill="x")
        self.display_frame.pack(fill="x")
        self.button_frame.pack(fill="x")

    def create_widgets(self):
        tk.Label(self.input_frame, text="Enter name: ").grid(row=0, column=0)

        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Button(
            self.input_frame,
            text="Create Account",
            command=self.create_account
        ).grid(row=0, column=2)

        self.name_label = tk.Label(self.display_frame, text="Name - ")
        self.name_label.pack()
   
    def login_validation(self):
        name = self.name_entry.get().strip()
        try:
            if not name:
                messagebox.showwarning("Warning", "Please enter a valid username. Try again!")
           
            else:
                self.borrower = Borrower(name)
                self.update_display()

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid username!")

    def create_account(self):
        self.login_validation()
   
    def update_display(self):
        if self.borrower is not None:
            self.name_label.config(text=f"Welcome {self.borrower.name}!")
            tk.Button(self.button_frame, text="Checkout Books", command=self.open_checkout).pack(fill='x')
            tk.Button(self.button_frame, text="Return Books", command=self.open_return).pack(fill='x')
            tk.Button(self.button_frame, text="View Books", command=self.view_books).pack(fill='x')

    def open_checkout(self):

        checkout = tk.Toplevel(root)
        checkout.title("Checkout book")
        checkout.geometry("30   0x150")

        tk.Label(checkout, text="Checkout a book:", font=("Arial", 12)).pack(pady=5)

        self.checkout_entry = tk.Entry(checkout, font=("Arial", 12))
        self.checkout_entry.pack(pady=5)

        def submit():
            book = self.checkout_entry.get().strip()
            
            if not book:
                messagebox.showwarning("Input Error", "Please enter the name of the book you would like to checkout.")
                return
            elif book not in self.book_catalogue.library_books:
                messagebox.showinfo("Error", f"{book} is not available!")
            else:
                messagebox.showinfo("Success", f"{book} has been checked out!")
                self.book_catalogue.check_out(book)
                self.borrower.user_checkout(book)
                checkout.destroy()

        tk.Button(checkout, text="Submit", command=submit, font=("Arial", 12)).pack(pady=10)
   
   
    def open_return(self):

        return_book = tk.Toplevel(root)
        return_book.title("Checkout book")
        return_book.geometry("300x150")

        tk.Label(return_book, text="Return a book:", font=("Arial", 12)).pack(pady=5)

        self.return_entry = tk.Entry(return_book, font=("Arial", 12))
        self.return_entry.pack(pady=5)

        def submit():
            book = self.return_entry.get().strip()
            if not book:
                messagebox.showwarning("Input Error", "Please enter the name of the book you would like to return.")
                return
            else:
                messagebox.showinfo("Success", f"You have returned {book}!")
                self.book_catalogue.return_books(book)
                self.borrower.user_return(book)
                return_book.destroy()

        tk.Button(return_book, text="Submit", command=submit, font=("Arial", 12)).pack(pady=10)
   
    def view_books(self):
        view_book = tk.Toplevel(root)
        view_book.title("View book catalogue")
        view_book.geometry("500x350")


        library_list = ", ".join(self.book_catalogue.library_books)
        user_list = ", ".join(self.borrower.user_books)

        self.lib_books_label = tk.Label(view_book, text="Book in the library:")
        self.user_books_label = tk.Label(view_book, text = f"Books you have taken out: {user_list}")
        self.lib_books_label.pack()
        self.user_books_label.pack()
       
        self.lib_books_label.config(text = f"Books in the library: {library_list}")
        self.user_books_label.config(text = f"Books you have taken out: {user_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()