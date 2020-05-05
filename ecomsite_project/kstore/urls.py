from django.urls import path
from .views import HomeView, ProductDetailView

from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('project/<int:pk>/', ProductDetailView.as_view(), name = 'product-detail'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('services/', views.services, name = 'services'),
    path('about-us/', views.about, name = 'about'),
    path('cart/<int:pk>/', views.cart, name = 'cart'),


]
