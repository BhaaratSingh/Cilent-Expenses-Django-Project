from django.contrib import admin

# Register your models here.

from .models import(Client,Expenses)

admin.site.register(Client)
admin.site.register(Expenses)