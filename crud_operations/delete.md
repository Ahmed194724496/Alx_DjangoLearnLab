from bookshelf.models import Book

# Delete a single record
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected output: Book deleted successfully

# Delete multiple records
Book.objects.filter(publication_year__lt=1900).delete()
# Expected output: All matching records deleted

# Delete all records
Book.objects.all().delete()
# Expected output: All books deleted 