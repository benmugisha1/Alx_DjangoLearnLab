from django.shortcuts import render
from .models import Book

# View to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all book instances
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.shortcuts import render, get_object_or_404
from .models import Library

# View to display library details
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)  # Query to get a specific library by primary key
    return render(request, 'relationship_app/library_detail.html', {'library': library})
