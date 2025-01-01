from django.contrib import admin # type: ignore
from .models import InventoryItem, Category

admin.site.register(InventoryItem)
admin.site.register(Category)
