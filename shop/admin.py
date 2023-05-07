from django.contrib import admin
from .models import User, Category, Shop, Product, ShopConnector, Cart, CartItems

# Register your models here.

admin.site.register(User)

admin.site.register(Product)
admin.site.register(ShopConnector)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','merchant','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','shop']

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['id','cart','product','quantity']