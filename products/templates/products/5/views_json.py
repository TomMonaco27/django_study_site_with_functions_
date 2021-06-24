'ctrl + R'
import os
import json

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)



def index(request):
    context = {
        'title' : 'GeekShop',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'GeekShop Product',
        'categories': [
            'Новинки',
            'Одежда',
            'Обувь',
            'Аксессуары',
            'Подарки',
        ]
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context['products'] = json.load(open(file_path, encoding='utf-8_Class_Basket'))
    return render(request, 'products/products.html', context)

# Тестовая страница
def test_context(request):
    context = {
        'title' : 'GeekShop',
        'header' : 'Добро пожаловать на сайт',
        'username' : ' Иван Иванов',
    }
    return render(request, 'products/test_context.html', context)

# Тестовая страница
def test(request):
    context = {
        'title' : 'GeekShop test',
        'header' : 'Добро пожаловать на сайт',
        'username' : ' Иван Иванов',
        'products' : [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6090',
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23725',
             'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3390',
             'about': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        ]
    }
    return render(request, 'products/test.html', context)