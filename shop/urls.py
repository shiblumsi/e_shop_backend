from django.urls import path

from . import views

urlpatterns = [
    path('category',views.ListCreateCategory.as_view(),name='list-create-category'),
    path('category/<int:pk>',views.DetailCategory.as_view(),name='detail-category'),
    path('createshop',views.CreateShop.as_view(),name='create-shop'),
    path('listshop',views.ListMerchantShop.as_view(),name='list-shop'),
    path('removeshop/<int:pk>',views.RemoveMerchantShop.as_view(),name='remove-shop'),
    path('connection/<int:shop_id>',views.ConnectionRequestSend.as_view(),name='connection-request'),
    path('response',views.ConnectionResponse.as_view(),name='connection-response'),
    path('addproduct',views.AddProduct.as_view(),name='add-product'),
    path('product/<int:pk>',views.AddProduct.as_view(),name='product-detail'),
    path('cart',views.CartListCreate.as_view(),name='list-create-cart'),
    path('cart/<int:pk>',views.CartDetail.as_view(),name='cart-detail'),
    path('addcartitem',views.AddCartItems.as_view(),name='add-cart-items'),
    #path('<int:cart_id>/cartitems/<int:pk>',views.CartItemsDetail.as_view(),name='list-create-cartitems'),
    path('cartitems/<int:pk>',views.CartItemsDetail.as_view(),name='detail-cartitems'),
]