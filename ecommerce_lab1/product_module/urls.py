from django.urls import path
from numpy import product
from .views import cart, productcat, removecart
from .views import index
urlpatterns = [
path('', index),
path('cart/', cart),
path('product/',productcat),
path('cart/remove/<int:id>', removecart),
]
