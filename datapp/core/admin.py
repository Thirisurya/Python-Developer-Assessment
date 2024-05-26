from django.contrib import admin
from .models import Account, Destination

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'account_id', 'account_name', 'app_secret_token', 'website')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('account', 'url', 'http_method')
