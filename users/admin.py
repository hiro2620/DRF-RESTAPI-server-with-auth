from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    model = User
    fieldsets = UserAdmin.fieldsets
    list_display = ['id', 'username']