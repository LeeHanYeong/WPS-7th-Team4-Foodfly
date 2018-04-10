from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            ),
        }),
        ('개인정보', {
            'fields': (
                'name',
                'email',
                'phone_number',
            ),
        }),
        ('접속정보', {
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
            ),
        }),
    )
    list_display = ('username', 'email', 'name', 'is_staff')
    search_fields = ('username', 'email', 'name')


admin.site.register(User, UserAdmin)
