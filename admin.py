# airplane/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Flight, Passenger, Reservation, Payment

# Define a custom admin class for User
class CustomUserAdmin(BaseUserAdmin):
    # List of fields to display in the change list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Fields to filter the change list on
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Fieldsets for displaying fields in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add fieldsets for adding a new user in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser'),
        }),
    )

    # Search fields for searching users in the admin interface
    search_fields = ('username', 'first_name', 'last_name', 'email')

    # Ordering of users in the admin interface
    ordering = ('username',)

    # Filter horizontal for ManyToMany fields in the admin interface
    filter_horizontal = ('groups', 'user_permissions',)

# Register models with their default admin classes
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
admin.site.register(Payment)

# Unregister the default UserAdmin and register User with CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
