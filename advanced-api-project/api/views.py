from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter  # Ensure this import is included
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters  # Import for filtering

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # Make sure to define this filter in filters.py

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]






 


