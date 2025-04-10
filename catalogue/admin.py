from django.contrib import admin
from .models import Category, Publisher, ComicBook, Review

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
    list_display = ('id', 'title', 'author', 'price', 'stock')
    list_filter = ('category', 'publisher')
    search_fields = ('title', 'author')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rating', 'comment', 'created')
    search_fields = ('rating', 'user')
