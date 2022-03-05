from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.models import Profile

User = get_user_model()


class UserProfileAdmin(UserAdmin):
    model = Profile


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

