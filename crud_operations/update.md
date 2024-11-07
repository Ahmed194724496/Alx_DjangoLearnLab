from bookshelf.models import Book

# Method 1: Update single record
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: Book title updated successfully

# Method 2: Update multiple records
Book.objects.filter(author="George Orwell").update(author="G. Orwell")
# Expected output: All matching records updated