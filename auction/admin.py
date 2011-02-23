from django.contrib import admin
from auction.models import *

class PurchaseInline(admin.TabularInline):
    model = Purchase

class PersonAdmin(admin.ModelAdmin):
    list_filter = [ 'table' ]
    list_display = [ Person.name, 'table', 'bid_number' ]
    search_fields = ['last_name', 'first_name', 'bid_number']

    inlines = [PurchaseInline]

    # crazy attempt -- roll this back!
    #def response_change(self, request, obj):
        #print "Here!"
        #return HttpResponseRedirect("/receipt/%d" % obj.id)




admin.site.register(Table)
admin.site.register(AuctionItem)
admin.site.register(Person,PersonAdmin)

