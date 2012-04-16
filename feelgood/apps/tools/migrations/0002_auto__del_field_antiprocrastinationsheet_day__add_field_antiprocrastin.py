# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'AntiProcrastinationSheet.day'
        db.delete_column('tools_antiprocrastinationsheet', 'day')

        # Adding field 'AntiProcrastinationSheet.date'
        db.add_column('tools_antiprocrastinationsheet', 'date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 1, 21)), keep_default=False)

        # Deleting field 'DailyActivitySchedule.day'
        db.delete_column('tools_dailyactivityschedule', 'day')

        # Adding field 'DailyActivitySchedule.date'
        db.add_column('tools_dailyactivityschedule', 'date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 1, 21)), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'AntiProcrastinationSheet.day'
        db.add_column('tools_antiprocrastinationsheet', 'day', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 1, 21)), keep_default=False)

        # Deleting field 'AntiProcrastinationSheet.date'
        db.delete_column('tools_antiprocrastinationsheet', 'date')

        # Adding field 'DailyActivitySchedule.day'
        db.add_column('tools_dailyactivityschedule', 'day', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 1, 21)), keep_default=False)

        # Deleting field 'DailyActivitySchedule.date'
        db.delete_column('tools_dailyactivityschedule', 'date')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 21, 10, 16, 24, 718612)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 21, 10, 16, 24, 718353)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tools.antiprocrastinationsheet': {
            'Meta': {'object_name': 'AntiProcrastinationSheet'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tools.antiprocrastinationsheetentry': {
            'Meta': {'object_name': 'AntiProcrastinationSheetEntry'},
            'activity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'actual_difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'actual_satisfaction': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predicted_difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'predicted_satisfaction': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'sheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['tools.AntiProcrastinationSheet']"})
        },
        'tools.bdc': {
            'Meta': {'object_name': 'BDC'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q_1': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_10': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_11': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_12': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_13': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_14': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_15': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_16': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_17': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_18': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_19': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_2': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_20': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_21': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_22': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_23': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_24': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_25': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_3': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_4': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_5': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_6': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_7': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_8': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'q_9': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tools.cognitivedistortion': {
            'Meta': {'object_name': 'CognitiveDistortion'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'tools.dailyactivityschedule': {
            'Meta': {'object_name': 'DailyActivitySchedule'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tools.dailyactivityscheduleentry': {
            'Meta': {'object_name': 'DailyActivityScheduleEntry'},
            'end': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prospective': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'retrospective': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['tools.DailyActivitySchedule']"}),
            'start': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'tools.novacoangerscale': {
            'Meta': {'object_name': 'NovacoAngerScale'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            's_1': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_10': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_11': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_12': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_13': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_14': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_15': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_16': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_17': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_18': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_19': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_2': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_20': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_21': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_22': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_23': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_24': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_25': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_3': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_4': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_5': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_6': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_7': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_8': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            's_9': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tools.triplecolumn': {
            'Meta': {'object_name': 'TripleColumn'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tools.triplecolumnentry': {
            'Meta': {'object_name': 'TripleColumnEntry'},
            'automatic_thought': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'cognitive_distortions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.CognitiveDistortion']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rational_response': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'triplecolumn': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['tools.TripleColumn']"})
        }
    }

    complete_apps = ['tools']
