from django.urls import path
from numpy import product
from .views import cart,  productcat, removecart,success_page,error_page
from .views import index
urlpatterns = [
path('', index),
path('cart/', cart),
path('product/',productcat),

path('cart/remove/<int:id>', removecart),
path('success_page/', success_page, name="success_page"),
path('error_page/', error_page, name="error_page"),
]
