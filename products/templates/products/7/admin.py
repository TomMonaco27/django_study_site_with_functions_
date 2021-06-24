# Register your models here.
# Регистрация моделей для отображения в админ-панеле

from django.contrib import admin


from products.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)



