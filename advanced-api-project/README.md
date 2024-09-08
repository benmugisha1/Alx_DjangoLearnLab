## API Features

### Filtering
You can filter the book list by title, author, or publication year:
- **Filter by title**: `/api/books/?title=example_title`
- **Filter by author**: `/api/books/?author__name=example_author`
- **Filter by publication year**: `/api/books/?publication_year=2023`

### Searching
Full-text search is enabled on the `title` and `author` fields:
- **Search by title or author**: `/api/books/?search=example_query`

### Ordering
You can order the book list by title or publication year:
- **Order by title (ascending)**: `/api/books/?ordering=title`
- **Order by publication year (descending)**: `/api/books/?ordering=-publication_year`
