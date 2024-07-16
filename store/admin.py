from django.contrib import admin

from .models import StoreProfile, Category, Product

# Register your models here.
admin.site.register(StoreProfile)
admin.site.register(Category)
admin.site.register(Product)