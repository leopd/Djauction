from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 100, null = True, blank = True)

    table = models.CharField(max_length=15)
    bid_number = models.IntegerField(unique = True)

    def __unicode__(self):
        return self.name()

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ['bid_number']


    def total(self):
        sum = 0
        for purchase in self.purchase_set.all():
            sum += purchase.amount
        return sum


class AuctionItem(models.Model):
    number = models.IntegerField(unique = True)
    name = models.CharField(max_length = 100)
    fair_value = models.FloatField(null = True, blank = True)

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return u"%s (Item #%s)" % (self.name, self.number)



PURCHASE_TYPES = (
        ('Donation', 'Raise the paddle donation'),
        ('Silent', 'Silent auction item'),
    )

class Purchase(models.Model):
    by_whom = models.ForeignKey(Person)
    type = models.CharField(max_length = 10, choices = PURCHASE_TYPES, default = 'Silent')
    item = models.ForeignKey(AuctionItem, null = True, blank = True)
    amount = models.FloatField()
    notes = models.CharField(max_length = 200, null = True, blank = True)

    def name(self):
        if self.item:
            return self.item
        return "Donation"

    def __unicode__(self):
        return u"%s purchased %s for %s" % (self.by_whom, self.item, self.amount)


