from django.contrib import admin
from .models import User, Category, Shop, Product, ShopConnector, Cart, CartItems

# Register your models here.

admin.site.register(User)




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

@admin.register(ShopConnector)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver','status']

@admin.register(Product)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','image','shop']