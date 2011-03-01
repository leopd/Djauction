from django.contrib import admin
from auction.models import *

class PurchaseInline(admin.TabularInline):
    model = Purchase
    extra = 1

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    list_filter = [ 'table' ]
    list_display = [ 'full_name', 'table', 'bid_number', Person.balance_due ]
    search_fields = ['full_name', 'bid_number']

    inlines = [PurchaseInline, PaymentInline]

    # crazy attempt -- roll this back!
    #def response_change(self, request, obj):
        #print "Here!"
        #return HttpResponseRedirect("/receipt/%d" % obj.id)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['by_whom', 'type', 'payment_number', 'amount', 'notes']
    list_filter = ['type']
    list_search = ['by_whom__name', 'by_whom__bid_number', 'notes']



class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['by_whom', 'type', 'amount', 'item', 'notes']
    list_filter = ['type']
    list_search = ['by_whom__name', 'by_whom__bid_number', 'item__name', 'notes']



admin.site.register(AuctionItem)
admin.site.register(Person,PersonAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Payment,PaymentAdmin)


