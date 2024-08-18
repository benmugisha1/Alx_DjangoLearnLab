from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(f"Book: {book.title}, Author: {book.author.name}")

# List all books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # Ensure this line is present
books_in_library = library.books.all()
for book in books_in_library:
    print(f"Library: {library.name}, Book: {book.title}")

# Retrieve the librarian for a specific library
librarian_for_library = library.librarian
print(f"Librarian for {library.name}: {librarian_for_library.name}")
