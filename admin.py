from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext, ugettext_lazy as _

from .forms import CreateUserForm, ChangeUserForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = ChangeUserForm
    add_form = CreateUserForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','staff','admin')
    list_filter = ('active','staff','admin')
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Personal info',{'fields':('email',)}),
        ('Permissions', {'fields': ('active','staff','admin')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password')}
        ),
        ('Personal info',{'fields':('email',)}),
        ('Permissions', {'fields': ('active','staff','admin')})
    )
    search_fields = ('username','email')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
