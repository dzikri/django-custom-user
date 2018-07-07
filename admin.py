from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm

class UserAdminForm(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email','active','admin')
    list_filter = ('active','admin')
    fieldsets = (
        ('Personal info', {'fields': ('username','email',)}),
        ('Password', {'fields': ('password',)}),
        ('Permissions', {'fields': ('staff','active','admin',)}),
    )

    add_fieldsets = (
        ('Personal info', {'fields': ('username','email',)}),
        ('Password', {'fields': ('password1', 'password2',)}),
        ('Permissions', {'fields': ('staff', 'active', 'admin',)}),
    )

    search_fields = ('username','email',)
    ordering = ('username','email',)
    filter_horizontal = ()


# Registering User model
admin.site.register(User, UserAdminForm)
