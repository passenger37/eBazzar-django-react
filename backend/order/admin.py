from django.contrib import admin
from .models import Order

@admin.register(Order)
class OdrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'is_paid', 'address')
    

