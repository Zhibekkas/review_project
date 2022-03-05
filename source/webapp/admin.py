from django.contrib import admin
from webapp.models import Product, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'product_pic']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'category', 'description', 'product_pic']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'review_text', 'rating', 'moderation_status', 'creation_date', 'update_date']
    list_filter = ['author', 'product']
    search_fields = ['author']
    fields = ['author', 'product', 'review_text', 'rating', 'moderation_status', 'creation_date', 'update_date']
    readonly_fields = ['creation_date', 'update_date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
