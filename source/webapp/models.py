from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
User = get_user_model()
DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Other'),
    ('good', 'Goods'),
    ('service', 'Services'),
    ('pharma', 'Medicines'),
    ('food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null= False, verbose_name='Product')
    category = models.CharField(max_length=30, blank=False, null=False,default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Category')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    product_pic = models.ImageField(null=True, blank=True, upload_to="product_pics", verbose_name="Picture")

    def __str__(self):
        return f'{self.name} - {self.category}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, verbose_name='Author')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Product', related_name='reviews')
    review_text = models.TextField(null=False, blank=False, verbose_name='Review')
    rating = models.PositiveBigIntegerField(null=False, blank=False, validators=(MinValueValidator(1), MaxValueValidator(5)))
    moderation_status = models.BooleanField(default=False, verbose_name='Moderation Status')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="Updated at")

    def __str__(self):
        return f'{self.author} - {self.product}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
