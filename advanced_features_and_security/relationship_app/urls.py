from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


# relationship_app/urls.py


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Assuming your custom registration view is in views.py


# relationship_app/urls.py

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Add other URL patterns as needed
]


# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    # Add other URL patterns as needed
]


from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('book/add/', views.add_book, name='add_book'),  # URL pattern for adding a book
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),  # URL pattern for editing a book
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),  # URL pattern for deleting a book
    # Add other URL patterns here if necessary
]

