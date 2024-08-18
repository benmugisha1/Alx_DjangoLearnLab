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


