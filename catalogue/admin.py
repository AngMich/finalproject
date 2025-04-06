from django.contrib import admin
from .models import Category, Publisher, ComicBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ('name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ComicBook)
class ComicBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'stock', 'is_featured')
    list_filter = ('is_featured', 'category', 'publisher')
    search_fields = ('title', 'author')
