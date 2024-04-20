from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', 'description')
    list_filter = ('price',)

admin.site.register(Book, BookAdmin)