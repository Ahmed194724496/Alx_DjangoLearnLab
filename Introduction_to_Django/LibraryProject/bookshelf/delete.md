# Delete Operation

## Command
```python
from bookshelf.models import Book

# Delete a specific book object
book.delete()

# Verify deletion by checking all books
Book.objects.all()

# Alternative ways to delete:
# Delete by specific ID
Book.objects.filter(id=1).delete()

# Delete multiple books matching criteria
Book.objects.filter(author="George Orwell").delete()

# Delete all books (use with caution!)
Book.objects.all().delete()
```