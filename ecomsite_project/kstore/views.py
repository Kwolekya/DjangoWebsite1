from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = 'kstore/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'kstore/product.html'
    context_object_name = 'products'


def cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'kstore/cart.html', context)

def checkout(request):
    return render(request, 'kstore/checkout.html')

def services(request):
    return render(request, 'kstore/services.html')

def about(request):
    return render(request, 'kstore/about.html')
