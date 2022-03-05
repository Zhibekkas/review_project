from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product, Review
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
        reviews = self.object.reviews.filter(moderation_status=True)
        context['reviews'] = reviews
        return context


class ProductAddView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'


