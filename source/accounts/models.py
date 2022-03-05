from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", verbose_name='Profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"Profile: {self.username}"

