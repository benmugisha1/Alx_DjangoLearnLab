import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Setup Django
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=['relationship_app', 'django.contrib.contenttypes'],
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}},
)
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == "__main__":
    print("Books by Author:")
    for book in books_by_author("Author Name"):
        print(book.title)

    print("Books in Library:")
    for book in books_in_library("Library Name"):
        print(book.title)

    print("Librarian for Library:")
    print(librarian_for_library("Library Name").name)
