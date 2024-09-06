from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer

class BookTests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create some books
        self.book1 = Book.objects.create(title='Book 1', author='Author 1', publication_year=2021)
        self.book2 = Book.objects.create(title='Book 2', author='Author 2', publication_year=2022)

    def test_book_list(self):
        # Test GET list endpoint
        url = reverse('book-list')
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_book_detail(self):
        # Test GET detail endpoint
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_book_create_authenticated(self):
        # Test POST create endpoint with authentication
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-list')
        data = {'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_update_authenticated(self):
        # Test PUT update endpoint with authentication
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book1.pk])
        data = {'title': 'Updated Book 1', 'author': 'Updated Author 1', 'publication_year': 2021}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_book_delete_authenticated(self):
        # Test DELETE endpoint with authentication
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filtering(self):
        # Test filtering functionality
        url = reverse('book-list') + '?title=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_searching(self):
        # Test searching functionality
        url = reverse('book-list') + '?search=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering(self):
        # Test ordering functionality
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')
