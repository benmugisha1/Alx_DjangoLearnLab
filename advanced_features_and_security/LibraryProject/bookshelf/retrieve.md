## Retrieve Operation

### Python Command:

```python
# Retrieve the book with the title "1984"
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
