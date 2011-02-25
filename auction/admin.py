from django.contrib import admin
from auction.models import *

class PurchaseInline(admin.TabularInline):
    model = Purchase

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_filter = [ 'table' ]
    list_display = [ Person.name, 'table', 'bid_number', Person.balance_due ]
    search_fields = ['full_name', 'bid_number']

    inlines = [PurchaseInline, PaymentInline]

    # crazy attempt -- roll this back!
    #def response_change(self, request, obj):
        #print "Here!"
        #return HttpResponseRedirect("/receipt/%d" % obj.id)


admin.site.register(AuctionItem)
admin.site.register(Person,PersonAdmin)

