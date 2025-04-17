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
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'})
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message', 'rows': 5})
    )