from django.urls import path
from .views import cart, removecart
from .views import index
urlpatterns = [
path('', index),
path('cart/', cart),
path('cart/remove/<int:id>', removecart),
]
