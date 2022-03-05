from django.shortcuts import get_object_or_404, redirect
from webapp.models import Product, Review
from webapp.forms import ReviewAddForm, ReviewUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewAddForm
    template_name = "reviews/create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.author = self.request.user
        review.product = product
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = ReviewUpdateForm

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})


class ReviewDeleteView(DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})

