from django.shortcuts import render, get_object_or_404
from .models import ComicBook, Category, Publisher
from django.db.models import Q

def get_descendant_categories(category):
    descendants = [category]
    for child in category.children.all():
        descendants += get_descendant_categories(child)
    return descendants

def catalogue_view(request):
    comics = ComicBook.objects.all()
    categories = Category.objects.all()
    publishers = Publisher.objects.all()

    # Search
    query = request.GET.get('q')
    if query:
        comics = comics.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query)
        )

    # Filters
    # Filters
    category_filter = request.GET.get('category')
    if category_filter:
        selected_category = get_object_or_404(Category, pk=category_filter)
        descendant_categories = get_descendant_categories(selected_category)
        comics = comics.filter(category__in=descendant_categories)

    publisher_filter = request.GET.get('publisher')
    if publisher_filter:
        comics = comics.filter(publisher__id=publisher_filter)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        comics = comics.filter(price__gte=min_price, price__lte=max_price)

    return render(request, 'catalogue/catalogue.html', {
        'comics': comics,
        'categories': categories,
        'publishers': publishers,
    })

def comic_detail_view(request, id):
    comic = get_object_or_404(ComicBook, pk=id)
    return render(request, 'catalogue/comic_detail.html', {'comic': comic})