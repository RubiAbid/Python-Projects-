import os
import json

# File to save/load data
FILE_NAME = "library.txt"

# Initialize the library list
library = []

# Load data from file
def load_library():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Error loading library data. Starting with an empty library.")
            return []
    return []

# Save data to file
def save_library():
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year! Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read it? (yes/no): ").lower()
    read = read_input == 'yes'

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }

    library.append(book)
    save_library()
    print(f"\n✅ '{title}' added to your library.\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    new_library = [book for book in library if book["Title"].lower() != title.lower()]
    if len(new_library) != len(library):
        library[:] = new_library
        save_library()
        print(f"\n✅ '{title}' removed from your library.\n")
    else:
        print(f"\n❌ Book titled '{title}' not found.\n")

# Search for a book
def search_book():
    query = input("Search by title or author: ").lower()
    results = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    if results:
        print("\n📚 Search Results:")
        for book in results:
            print_book(book)
    else:
        print("\n❌ No matching books found.")

# Display all books
def display_books():
    if not library:
        print("\n📂 Your library is empty.")
    else:
        print("\n📚 Your Book Collection:")
        for book in library:
            print_book(book)

# Display a single book in a nice format
def print_book(book):
    print(f"- {book['Title']} by {book['Author']} ({book['Year']}) | Genre: {book['Genre']} | {'Read' if book['Read'] else 'Unread'}")

# Display statistics
def show_statistics():
    total_books = len(library)
    if total_books == 0:
        print("\n📊 No books in your library.")
        return
    read_books = sum(book['Read'] for book in library)
    percentage = (read_books / total_books) * 100
    print(f"\n📊 Library Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books} ({percentage:.2f}%)")

# Main menu loop
def menu():
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            print("👋 Exiting... Your data has been saved.")
            save_library()
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
library = load_library()
menu()
