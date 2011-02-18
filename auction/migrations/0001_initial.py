# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Table'
        db.create_table('auction_table', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('captain', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='captain_of', null=True, to=orm['auction.Person'])),
        ))
        db.send_create_signal('auction', ['Table'])

        # Adding model 'Person'
        db.create_table('auction_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.Table'])),
            ('bid_number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal('auction', ['Person'])

        # Adding model 'AuctionItem'
        db.create_table('auction_auctionitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fair_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('auction', ['AuctionItem'])

        # Adding model 'Purchase'
        db.create_table('auction_purchase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('by_whom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.Person'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='Silent', max_length=10)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.AuctionItem'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('auction', ['Purchase'])


    def backwards(self, orm):
        
        # Deleting model 'Table'
        db.delete_table('auction_table')

        # Deleting model 'Person'
        db.delete_table('auction_person')

        # Deleting model 'AuctionItem'
        db.delete_table('auction_auctionitem')

        # Deleting model 'Purchase'
        db.delete_table('auction_purchase')


    models = {
        'auction.auctionitem': {
            'Meta': {'ordering': "['number']", 'object_name': 'AuctionItem'},
            'fair_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'auction.person': {
            'Meta': {'ordering': "['bid_number']", 'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bid_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Table']"})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'by_whom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.AuctionItem']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Silent'", 'max_length': '10'})
        },
        'auction.table': {
            'Meta': {'ordering': "['number']", 'object_name': 'Table'},
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'captain_of'", 'null': 'True', 'to': "orm['auction.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['auction']
