from .models import ComicBook
from django.db.models import Q

def get_recommended_comics(comic, limit=4):
    return ComicBook.objects.filter(
        Q(genre=comic.genre) | Q(category=comic.category)
    ).exclude(id=comic.id).order_by('?')[:limit]
