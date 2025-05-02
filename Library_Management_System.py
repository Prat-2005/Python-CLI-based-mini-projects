# LIBRARY MANAGEMENT SYSTEM

class BookNotAvailableError(Exception):
    def __init__(self, book, msg):
        self.book = book
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"\"{self.book}\" is not available."

def add_books(book):
    if book not in books:
        books.append(book)
    else:
        print(f"{book} book is already available in the list.")

def view_books():
    books.sort()
    for srno, bk in enumerate(books):
        print(f"{srno + 1}. {bk}")
    print()

def borrow_books(book):
    if book in books:
        books.remove(book)
    else:
        raise BookNotAvailableError(book)

def return_books(book):
    if book not in books:
        books.append(book)
    else:
        print(f"{book} book is already available in the list.")

books = ["The Silent Patient", "Sapiens: A Brief History of Humankind", "Project Hail Mary", "The Midnight Library", "Atomic Habits"]

while True:
    print("Choose any one:")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    try:
        choice = input("Enter your choice:")

        if choice == '1':
           print("Books List:")
           view_books()
        elif choice == '2':
            n = int(input("How many books you want to borrow?:"))
            for _ in range(n):
               book_name = input("Enter book name:")
               if not book_name.isdigit():
                   borrow_books(book_name.strip().title())
               else:
                   raise ValueError("Number instead of book name")
               print(f"Request Approved! You burrowed a book {book_name} from the list.\n")
        elif choice == '3':
            n = int(input("How many books you want to return?:"))
            for _ in range(n):
               book_name = input("Enter book name:")
               if not book_name.isdigit():
                   return_books(book_name.strip().title())
               else:
                   raise ValueError("Number instead of book name") 
               print(f"Book Returned Successfully! You returned a book {book_name} which was borrowed.\n")
        elif choice == '4':
            n = int(input("how many books you want to add on in the list?:"))
            for _ in range(n):
                book_name = input("Enter new books one by one:")
                if not book_name.isdigit():
                    add_books(book_name.strip().title())
                else:
                    raise ValueError("Number instead of book name")
                print(f"{book_name} added successfully in the list.\n")
        elif choice == '5':
            isexit = input("Are you sure you want to exit (y/n)?:")
            if isexit == "y":
                break
        else:
           print("Invalid choice. Please enter a number between 1 - 5.\n")
    except ValueError as e:
        print(f"ERROR! {e}.\n")
    except BookNotAvailableError as e:
        print(f"ERROR! {e}.\n")