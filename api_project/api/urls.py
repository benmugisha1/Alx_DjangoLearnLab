from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
]


from django.contrib import admin
from django.urls import path, include  # Import include function

urlpatterns = [
    path('admin/', admin.site.urls),        # Admin URL
    path('api/', include('api.urls')),       # Include the api app's URLs
]
