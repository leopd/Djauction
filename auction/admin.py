from django.contrib import admin
from auction.models import *

class PurchaseInline(admin.TabularInline):
    model = Purchase

class PersonAdmin(admin.ModelAdmin):
    list_filter = [ 'table' ]
    list_display = [ Person.name, 'table', 'bid_number' ]
    search_fields = ['last_name', 'first_name']

    inlines = [PurchaseInline]


admin.site.register(Table)
admin.site.register(Person,PersonAdmin)

