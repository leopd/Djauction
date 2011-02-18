import csv
from django.core.management.base import BaseCommand, CommandError

from auction.models import *

class Command(BaseCommand):
    args = '<filename.csv>'
    help = 'Imports a CSV file into a table.'

    def handle(self, filename, *args, **options):
        klass = Person
        fh = open(filename,'rU')
        reader = csv.DictReader(fh,dialect='excel')

        print "Importing %s data from file %s" % (klass, filename)
        ignores = {}

        for row in reader:
            #print("Read %s" % row)
            obj = klass()
            for key in row.keys():
                if obj.__dict__.keys().__contains__(key):
                    obj.__setattr__(key,row[key])
                else:
                    if not ignores.get(key,None):
                        ignores[key]=True
                        print "Ignoring column %s" % key
            obj.save()
            print "Created %s" % obj
            




