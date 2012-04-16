# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CognitiveDistortion'
        db.create_table('tools_cognitivedistortion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('tools', ['CognitiveDistortion'])

        # Adding model 'BDC'
        db.create_table('tools_bdc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('q_1', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_2', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_3', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_4', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_5', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_6', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_7', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_8', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_9', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_10', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_11', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_12', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_13', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_14', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_15', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_16', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_17', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_18', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_19', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_20', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_21', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_22', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_23', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_24', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('q_25', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal('tools', ['BDC'])

        # Adding model 'NovacoAngerScale'
        db.create_table('tools_novacoangerscale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('s_1', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_2', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_3', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_4', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_5', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_6', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_7', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_8', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_9', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_10', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_11', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_12', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_13', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_14', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_15', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_16', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_17', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_18', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_19', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_20', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_21', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_22', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_23', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_24', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('s_25', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal('tools', ['NovacoAngerScale'])

        # Adding model 'TripleColumn'
        db.create_table('tools_triplecolumn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('tools', ['TripleColumn'])

        # Adding model 'TripleColumnEntry'
        db.create_table('tools_triplecolumnentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('triplecolumn', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['tools.TripleColumn'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('automatic_thought', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('rational_response', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('tools', ['TripleColumnEntry'])

        # Adding M2M table for field cognitive_distortions on 'TripleColumnEntry'
        db.create_table('tools_triplecolumnentry_cognitive_distortions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triplecolumnentry', models.ForeignKey(orm['tools.triplecolumnentry'], null=False)),
            ('cognitivedistortion', models.ForeignKey(orm['tools.cognitivedistortion'], null=False))
        ))
        db.create_unique('tools_triplecolumnentry_cognitive_distortions', ['triplecolumnentry_id', 'cognitivedistortion_id'])

        # Adding model 'DailyActivitySchedule'
        db.create_table('tools_dailyactivityschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('tools', ['DailyActivitySchedule'])

        # Adding model 'DailyActivityScheduleEntry'
        db.create_table('tools_dailyactivityscheduleentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['tools.DailyActivitySchedule'])),
            ('start', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('end', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('prospective', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('retrospective', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('tools', ['DailyActivityScheduleEntry'])

        # Adding model 'AntiProcrastinationSheet'
        db.create_table('tools_antiprocrastinationsheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('tools', ['AntiProcrastinationSheet'])

        # Adding model 'AntiProcrastinationSheetEntry'
        db.create_table('tools_antiprocrastinationsheetentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['tools.AntiProcrastinationSheet'])),
            ('activity', self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True)),
            ('predicted_difficulty', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
            ('predicted_satisfaction', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
            ('actual_difficulty', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
            ('actual_satisfaction', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
        ))
        db.send_create_signal('tools', ['AntiProcrastinationSheetEntry'])


    def backwards(self, orm):
        
        # Deleting model 'CognitiveDistortion'
        db.delete_table('tools_cognitivedistortion')

        # Deleting model 'BDC'
        db.delete_table('tools_bdc')

        # Deleting model 'NovacoAngerScale'
        db.delete_table('tools_novacoangerscale')

        # Deleting model 'TripleColumn'
        db.delete_table('tools_triplecolumn')

        # Deleting model 'TripleColumnEntry'
        db.delete_table('tools_triplecolumnentry')

        # Removing M2M table for field cognitive_distortions on 'TripleColumnEntry'
        db.delete_table('tools_triplecolumnentry_cognitive_distortions')

        # Deleting model 'DailyActivitySchedule'
        db.delete_table('tools_dailyactivityschedule')

        # Deleting model 'DailyActivityScheduleEntry'
        db.delete_table('tools_dailyactivityscheduleentry')

        # Deleting model 'AntiProcrastinationSheet'
        db.delete_table('tools_antiprocrastinationsheet')

        # Deleting model 'AntiProcrastinationSheetEntry'
        db.delete_table('tools_antiprocrastinationsheetentry')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 21, 10, 11, 59, 764872)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 21, 10, 11, 59, 764802)'}),
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
            'day': ('django.db.models.fields.DateField', [], {}),
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
            'day': ('django.db.models.fields.DateField', [], {}),
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
