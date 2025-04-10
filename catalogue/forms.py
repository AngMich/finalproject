from django import forms
from .models import ComicBook, Review

class ComicBookForm(forms.ModelForm):
    class Meta:
        model = ComicBook
        fields = [
            'title',
            'author',
            'publisher',
            'category',
            'genre',
            'price',
            'stock',
            'image',
            'description',
            'is_featured',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'is_featured': forms.CheckboxInput(),
        }


class reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
