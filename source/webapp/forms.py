from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product', 'moderation_status']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product']

