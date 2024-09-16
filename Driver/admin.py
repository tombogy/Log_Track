# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LogisticUser
# from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = LogisticUser
    list_display = ('email', 'name', 'mobile', 'user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'name', 'mobile')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'mobile', 'user_type', 'liscence')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile', 'user_type', 'liscence', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(LogisticUser, CustomUserAdmin)
