from django.shortcuts import render
from .models import Book

# View to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all book instances
    return render(request, 'relationship_app/list_books.html', {'books': books})
