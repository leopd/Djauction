from django.db import models


PAYMENT_CHOICES = (
        ('Credit Card', 'Credit Card'),
        ('Check', 'Check'),
        ('Cash', 'Cash'),
        ('Other', 'Other'),
        ('None yet', 'None yet'),
    )

class Person(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.CharField(max_length = 100, null = True, blank = True)
    address = models.TextField(null = True, blank = True)

    table = models.CharField(max_length=15)
    bid_number = models.IntegerField(unique = True)

    payment_type = models.CharField(max_length = 20, choices = PAYMENT_CHOICES, default = 'None yet')
    payment_number = models.CharField("Check number or Last 4 of credit card", max_length = 100, null = True, blank = True)

    general_notes = models.TextField(null = True, blank = True)

    def __unicode__(self):
        return self.name()

    def name(self):
        return self.full_name

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
        ('Silent auction item','Silent auction item'),
        ('Ticket Purchase','Ticket Purchase'),
        ('Raise the Paddle','Raise the Paddle'),
        ('Orphan Sponsorship','Orphan Sponsorship'),
        ('Clinic Sponsorship','Clinic Sponsorship'),
        ('General Donation','General Donation'),
        ('Clinic Donation','Clinic Donation'),
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


