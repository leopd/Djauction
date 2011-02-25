# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Person.payment_type'
        db.add_column('auction_person', 'payment_type', self.gf('django.db.models.fields.CharField')(default='None yet', max_length=20), keep_default=False)

        # Adding field 'Person.payment_number'
        db.add_column('auction_person', 'payment_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Person.general_notes'
        db.add_column('auction_person', 'general_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Person.payment_type'
        db.delete_column('auction_person', 'payment_type')

        # Deleting field 'Person.payment_number'
        db.delete_column('auction_person', 'payment_number')

        # Deleting field 'Person.general_notes'
        db.delete_column('auction_person', 'general_notes')


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
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bid_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'general_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'None yet'", 'max_length': '20'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'table': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'by_whom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.AuctionItem']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Silent'", 'max_length': '10'})
        }
    }

    complete_apps = ['auction']
