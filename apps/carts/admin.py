from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class Cartmode(admin.ModelAdmin):
    fields = ['user', 'product', 'quantity']
    list_filter = []
    list_displsy = fields
    search_fields = ['user','product']
