from django.contrib import admin

# Register your models here.
from records.models import Property, Client, Rent

admin.site.register(Property)
admin.site.register(Client)
admin.site.register(Rent)
