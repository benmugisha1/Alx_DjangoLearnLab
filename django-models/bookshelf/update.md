
### `update.md`
```markdown
## Update Operation

### Python Command:

```python
# Update the title of the book from '1984' to 'Nineteen Eighty-Four'
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
