from django.contrib import admin
from .models import Slider, Medicines, OrderMedicine, Orders

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_display_links = ['id', 'image']

@admin.register(Medicines)
class MedicinesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salt', 'price', 'discounted_price', 'quantity', 'image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'salt']
    list_filter = ['quantity']

@admin.register(OrderMedicine)
class OrderMedicineAdmin(admin.ModelAdmin):
    list_display = ['id', 'medicine', 'quantity']
    list_display_links = ['id', 'medicine']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'address', 'order_status', 'created_date']
    list_display_links = ['id', 'name']
    list_filter = ['order_status', 'created_date']
    search_fields = ['name', 'phone', 'address', 'note']
    filter_horizontal = ['medicines']
    readonly_fields = ['created_date']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('medicines__medicine')
        return qs
