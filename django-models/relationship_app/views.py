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
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# relationship_app/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate view name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
