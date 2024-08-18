from django.shortcuts import render
from django.views.generic.detail import DetailView  # Ensure this line is present
from .models import Author, Book, Library, Librarian

# Example DetailView for a Book
class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'

# Example DetailView for an Author
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'

# Other views can be added below
