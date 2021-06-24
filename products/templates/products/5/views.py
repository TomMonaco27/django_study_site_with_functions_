'''
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
'''

from django.shortcuts import render

from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллер = вьюхи = представления
def index(request):
    context = {
        'title' : 'GeekShop',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'GeekShop Products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)
