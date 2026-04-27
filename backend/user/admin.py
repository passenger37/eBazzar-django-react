from django.contrib import admin
from .models import (User,
                    Address)

class UserAdmin(admin.ModelAdmin):
    list_display = ('profile', 'mobile_number', 'gender')
admin.site.register(User, UserAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=('user','city','postal_code')
admin.site.register(Address, AddressAdmin)