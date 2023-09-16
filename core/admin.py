from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)

from.models import (
    CustomUser
)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'register_number',
    ]
    fieldsets = [
        [
            None,
            {
                'fields': [
                    'password'
                ]
            }
        ],
        [
            'Personal Information',
            {
                'fields': [
                    'picture',
                ]
            }
        ],
        [
            'Permissions',
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                ]
            }
        ],
        [
            'Important Dates',
            {
                'fields': [
                    'last_login',
                    'date_joined'
                ]
            }
        ]
    ]
