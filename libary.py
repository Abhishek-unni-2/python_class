class Library:
    def __init__(self):
        self.books = ["DevOps", "Python", "AI", "Linux"]

    def list_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print("-", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed: {book_name}")
        else:
            print("Sorry, book not available.")
        self.list_books()  # Show updated list

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You returned: {book_name}")
        self.list_books()  # Show updated list

    def change_book_name(self, old_name, new_name):
        if old_name in self.books:
            index = self.books.index(old_name)
            self.books[index] = new_name
            print(f"Book name changed from '{old_name}' to '{new_name}'")
        else:
            print(f"Book '{old_name}' not found.")
        self.list_books()  # Show updated list

# Using the class
lib = Library()

# Menu
while True:
    print("\n1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Change Book Name")
    print("5. Exit")
    
    choice = input("Choose option: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        name = input("Enter book name to borrow: ")
        lib.borrow_book(name)
    elif choice == "3":
        name = input("Enter book name to return: ")
        lib.return_book(name)
    elif choice == "4":
        old = input("Enter old book name: ")
        new = input("Enter new book name: ")
        lib.change_book_name(old, new)
    elif choice == "5":
        print("Bye! Visit again.")
        break
    else:
        print("Invalid option. Try again.")
