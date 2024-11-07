# Update Operation

## Command
```python
# First, retrieve the book you want to update
book = Book.objects.get(title="1984")

# Then update its properties
book.title = "Nineteen Eighty-Four"
book.save()
ٍ