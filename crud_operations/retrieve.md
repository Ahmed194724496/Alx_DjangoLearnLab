from bookshelf.models import Book

# Get a single book by ID
book = Book.objects.get(id=1)

# Get a book by title
book = Book.objects.get(title="1984")

# Get all books
all_books = Book.objects.all()

# Filter books with conditions
orwell_books = Book.objects.filter(author="George Orwell")
old_books = Book.objects.filter(publication_year__lt=1950)

# Complex queries
books = Book.objects.filter(
    publication_year__gte=1900
).exclude(
    author="Unknown"
).order_by('-publication_year')