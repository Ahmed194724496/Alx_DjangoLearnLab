from django.contrib import admin
from .models import Book

# Register the Book model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize the display columns
    list_filter = ('author',)  # Enable filtering by author
    search_fields = ('title', 'author')  # Enable search functionality
