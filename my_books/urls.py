from django.urls import path
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from . import views
from .views import order_books
from .views import add_to_cart, remove_from_cart, update_cart, view_cart, clear_cart

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('order_books/', order_books, name='order_books'),
    path('cart/', view_cart, name='cart'),
    
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
]