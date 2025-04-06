from django import forms
from .models import ComicBook

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
