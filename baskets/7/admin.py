# Register your models here.
from django.contrib import admin

from baskets.models import Basket

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
