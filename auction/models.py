from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    captain = models.ForeignKey('Person',null = True, blank = True, related_name='captain_of')
    
    def __unicode__(self):
        return "Table %s" % self.number

    class Meta:
        ordering = ['number']


class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 100, null = True, blank = True)

    table = models.ForeignKey(Table)
    bid_number = models.IntegerField()

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



PURCHASE_TYPES = (
        ('Paddle', 'Raise the paddle'),
        ('Silent', 'Silent auction item'),
    )


class Purchase(models.Model):
    by_whom = models.ForeignKey(Person)
    type = models.CharField(max_length = 10, choices = PURCHASE_TYPES, default = 'Silent')
    item_number = models.CharField(max_length = 5, null = True, blank = True)
    amount = models.FloatField()
    notes = models.CharField(max_length = 200, null = True, blank = True)

    def name(self):
        if self.item_number:
            return "Silent Auction Item #%s" % (self.item_number)
        return "Raise the paddle donation"


