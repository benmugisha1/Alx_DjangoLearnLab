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
            return redirect('home')  # Update 'home' to the name of your homepage view
    else:
        form = UserCreationForm()
    
    # Render the 'register.html' template
    return render(request, 'register.html', {'form': form})

# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper functions to check roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

