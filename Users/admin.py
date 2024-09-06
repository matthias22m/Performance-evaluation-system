from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Group, Profile
# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Employee, Group, Profile

class EmployeeAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'unit', 'gender','phone_number', 'position', 'job_title', 'salary')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'unit', 'gender', 'phone_number', 'position', 'job_title', 'salary', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Group)
admin.site.register(Profile)
