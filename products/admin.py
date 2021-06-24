# Register your models here.
# Регистрация моделей для отображения в админ-панеле
from django.contrib import admin


from products.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity', 'category'))
    readonly_fields = ('description',)
    ordering = ('-price',)
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    ordering = ('id',)
    search_fields = ('name',)



