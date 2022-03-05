from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product, Review
from django.db.models import Avg


class IndexView(ListView):
    template_name = 'products/index_view.html'
    context_object_name = 'products'
    model = Product
    ordering = ['category', 'name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        for product in Product.objects.all():
            average = Review.objects.filter(product__id=product.id).aggregate(Avg('rating'))
        context['average'] = average
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.order_by("-creation_date")
        context['reviews'] = reviews
        return context


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('webapp:index')


