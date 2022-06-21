from django.contrib import admin
from .models import Stock, Purchase
 
# Register your models here.
 
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display=("item","quantity")
 
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('available_item','available_quantity')