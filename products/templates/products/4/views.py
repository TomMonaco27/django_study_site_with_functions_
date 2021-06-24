'''
<a href="#" class="list-group-item">Новинки</a>
                    <a href="#" class="list-group-item">Одежда</a>
                    <a href="#" class="list-group-item">Обувь</a>
                    <a href="#" class="list-group-item">Аксессуары</a>
                    <a href="#" class="list-group-item">Подарки</a>
'''

from django.shortcuts import render

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
        'categories' : [
            'Новинки',
            'Одежда',
            'Обувь',
            'Аксессуары',
            'Подарки',
            ],
        'products' : [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6090',
             'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни!',
             'image': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23725',
             'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель!',
             'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3390',
             'about': 'Материал с плюшевой текстурой. Удобный и мягкий!',
             'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
        ]

    }
    return render(request, 'products/products.html', context)
