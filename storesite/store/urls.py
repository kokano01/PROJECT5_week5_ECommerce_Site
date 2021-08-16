from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='store-index'),
    path('register/', views.registerPage, name = 'store-register'),
    path('login/', views.loginPage, name = 'store-login'),
    path('logout/', views.logoutUser, name ='store-logout'),
    path('products/',  views.productPage, name = 'store-productpage'),
    path('products/<int:item_id>',  views.individualItem, name = 'store-info'),
    path('products/addtocart/item',  views.addtoCart, name = 'store-cart'),
    path('products/showcart/',  views.myCart, name = 'store-mycart'),
    
]