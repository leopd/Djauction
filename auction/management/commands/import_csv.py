import csv
import sys
import re
from django.core.management.base import BaseCommand, CommandError

import auction.models

class Command(BaseCommand):
    args = '<classname> <filename.csv>'
    help = 'Imports a CSV file into a table.'

    def handle(self, classname, filename, *args, **options):
        if re.search(r'\W',classname):
            print("First parameter must be the name of a model to import like 'Person'. %s does not work" % classname)
            print("Try...")
            print(dir(auction.models))
            sys.exit(-1)
        klass = eval("auction.models.%s" % classname)
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
            




