from relationship_app.models import Author, Book

# Assuming we are querying for an author with the name "John Doe"
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)
from relationship_app.models import Library

# Assuming we are querying for a library with the name "Central Library"
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)
from relationship_app.models import Library, Librarian

# Assuming we are querying for a library with the name "Central Library"
library = Library.objects.get(name="Central Library")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
