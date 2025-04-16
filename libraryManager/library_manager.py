# Initialize the library list
library = []

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read = input("Have you read it? (yes/no): ").lower()

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read == "yes"
    }

    library.append(book)
    print(f"✅ '{title}' added to your library.\n")

# Function to show all books
def display_books():
    if not library:
        print("📂 Your library is empty.\n")
    else:
        print("\n📚 Your Book Collection:")
        for book in library:
            read_status = "Read" if book["Read"] else "Unread"
            print(f"- {book['Title']} by {book['Author']} ({book['Year']}) | Genre: {book['Genre']} | {read_status}")

# Function to search a book
def search_book():
    query = input("Search by title or author: ").lower()
    found = False
    for book in library:
        if query in book["Title"].lower() or query in book["Author"].lower():
            read_status = "Read" if book["Read"] else "Unread"
            print(f"- {book['Title']} by {book['Author']} ({book['Year']}) | Genre: {book['Genre']} | {read_status}")
            found = True
    if not found:
        print("❌ Book not found.")

# Function to show menu
def menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Choose 1-4: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Start the program
menu()
