from django.core.management.base import BaseCommand, CommandError

from auction.models import *


class Command(BaseCommand):
    args = '<num_tables>'
    help = 'Creates table objects'

    def handle(self, num_tables, *args, **options):
        num_tables = int(num_tables)
        for n in range(1,num_tables+1):
            t = Table(number = n)
            t.save()
        print "Created %d tables" % num_tables
