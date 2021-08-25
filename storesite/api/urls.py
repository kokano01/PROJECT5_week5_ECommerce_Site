from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('items/', views.items, name='api-items'),
    path('items/<int:item_id>/', views.individualItem, name='api-individualitem'),
]