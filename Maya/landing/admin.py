from django.contrib import admin
from .models import ExtendedUser, Interest, UsersInterest

# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Interest)
admin.site.register(UsersInterest)

