# Retrieve Operation

## Command
```python
# Get all books
Book.objects.all()

# Get a specific book by ID
Book.objects.get(id=1)

# Get a specific book by title
Book.objects.get(title="1984")

# Filter books by a condition
Book.objects.filter(author="George Orwell")

# Get first book that matches a condition
Book.objects.filter(published_year=1949).first()ٍ