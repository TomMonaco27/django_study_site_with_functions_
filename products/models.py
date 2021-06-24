from django.db import models

# Create your models here.
# модели = таблицы
# Хранит информацию о таблицах в нашей будущей базе данных.
# Создаем классы, которые потом будут преобразовываться в таблицы в БД.
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py shell

# from products.models import ProductCategory, Product - импортирование таблиц из нашего проекта
# product_category = ProductCategory(name='Одежда', description='Описание для класса одежды') - cоздаем объект класса
# product_category.save() - выполняется SQL-запрос и отправляет данные в таблицу(сохраняет объект в БД)

# QuerySet - это набор запросов, который представляет собой набор объектов из базы данных
# Методы QuerySet:
# all() - возвращает список всех объектов из БД
# filter() - возвращает список объектов из БД по определенному признаку
# get() - возвращает объект из БД
# create() - создает объект в БД
# пример, product_category = ProductCategory.objects.get(id=1)
# пример, product_category = ProductCategory.objects.create(name='Новинки')
# пример, product_category = ProductCategory.objects.all()
# categories.first()
# categories.last()
# categories.count()
# product_category.delete()
# пример, product_category = ProductCategory.objects.filter(description=None)
# print(ProductCategory.objects.all().query) - получение запроса в виде SQL

# python manage.py createsuperuser - создание админ-пользователя

# ALLOWED_HOSTS = ['localhost', '127.0.0.1']  ALLOWED_HOSTS = ['*']

#python manage.py dumpdata products.ProductCategory > category.json
# python manage.py dumpdata products.Product > goods.json


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True) # описание может быть или отсутствовать

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    # 'product_images - папка для хранения (куда загружать) картинки
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # category = models.ForeignKey(ProductCategory, related_name= '' , on_delete=models.PROTECT)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} | {self.category.name}'