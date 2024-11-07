from bookshelf.models import Book

# Method 1: Using create()
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected output: New book created successfully

# Method 2: Using instance creation and save()
book = Book(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book.save()
# Expected output: New book created successfully