## Delete Operation

### Python Command:

```python
# Import the Book model from bookshelf app
from bookshelf.models import Book

# Retrieve the book with the title "1984"
book = Book.objects.get(title="1984")

# Delete the retrieved book
book.delete()
