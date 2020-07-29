from django.contrib import admin
from .models import Item, Account

# Register your models here.
# admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass