# CRUD Operations Documentation

## Create Operation

### Command
python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

### Expected Output
plaintext
# No output, but you can confirm the book has been created.

## Retrieve Operation
### Command
python
all_books = Book.objects.all()
print(all_books)

### Expected Output
plaintext
<QuerySet [<Book: 1984>]>ٍ

## Update Operation
### Command
python
book.title = "Nineteen Eighty-Four"
book.save()

### Expected Output
plaintext
# No output, but you can confirm the title has been updated by retrieving the book again.

## Delete Operation
### Command
python
book.delete()
all_books_after_deletion = Book.objects.all()
print(all_books_after_deletion)

### Expected Output
plaintext
<QuerySet []>