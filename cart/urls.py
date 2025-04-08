from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:comic_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
