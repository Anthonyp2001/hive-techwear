from django.contrib import admin
from .models import User

@admin.register(User)
class UserModel(admin.ModelAdmin):
    Fields = ['name', 'email', 'token', 'token_expires']
    list_filter = []
    list_display = Fields
    search_fields = ['name', 'email']
    

