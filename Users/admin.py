from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Group, Profile
# Register your models here.

Employee = get_user_model()

admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Profile)
