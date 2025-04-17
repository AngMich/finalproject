from django.shortcuts import render, get_object_or_404, redirect
from .models import ComicBook, Category, Publisher, Review
from django.db.models import Q
from .forms import reviews
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .logic import get_recommended_comics
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        messages.success(request, "Thank you for reaching out. We'll get back to you soon.")
        return redirect('catalogue:contact')
    return render(request, 'catalogue/contact.html', {'form': form})


def about_view(request):
    return render(request, 'catalogue/about.html')


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
    user_review = None
    recommended = get_recommended_comics(comic)
    return render(request, 'catalogue/comic_detail.html', {
        'comic': comic,
        'recommended_comics': recommended,
    })
    if request.user.is_authenticated:
        user_review = Review.objects.filter(user=request.user, comic=comic).first()

    return render(request, 'catalogue/comic_detail.html', {
        'comic': comic,
        'user_review': user_review,
    })

@login_required
def add_review(request, comic_id):
    comic = get_object_or_404(ComicBook, id=comic_id)

    # Prevent duplicate reviews
    if Review.objects.filter(user=request.user, comic=comic).exists():
        messages.warning(request, "You have already submitted a review for this comic.")
        return redirect('catalogue:comic_detail', id=comic.id)

    if request.method == 'POST':
        form = reviews(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.comic = comic
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect('catalogue:comic_detail', id=comic.id)
    else:
        form = reviews()

    return render(request, 'catalogue/add_review.html', {
        'form': form,
        'comic': comic,
    })
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    comic_id = review.comic.id
    review.delete()
    return redirect('catalogue:comic_detail', id=comic_id)
