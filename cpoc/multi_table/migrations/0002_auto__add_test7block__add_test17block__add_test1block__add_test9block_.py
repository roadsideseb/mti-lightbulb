# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test7Block'
        db.create_table(u'multi_table_test7block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test7Block'])

        # Adding model 'Test17Block'
        db.create_table(u'multi_table_test17block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test17Block'])

        # Adding model 'Test1Block'
        db.create_table(u'multi_table_test1block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test1Block'])

        # Adding model 'Test9Block'
        db.create_table(u'multi_table_test9block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test9Block'])

        # Adding model 'Test10Block'
        db.create_table(u'multi_table_test10block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test10Block'])

        # Adding model 'Test6Block'
        db.create_table(u'multi_table_test6block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test6Block'])

        # Adding model 'Test3Block'
        db.create_table(u'multi_table_test3block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test3Block'])

        # Adding model 'Test0Block'
        db.create_table(u'multi_table_test0block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test0Block'])

        # Adding model 'Test19Block'
        db.create_table(u'multi_table_test19block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test19Block'])

        # Adding model 'Test2Block'
        db.create_table(u'multi_table_test2block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test2Block'])

        # Adding model 'Test12Block'
        db.create_table(u'multi_table_test12block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test12Block'])

        # Adding model 'Test18Block'
        db.create_table(u'multi_table_test18block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test18Block'])

        # Adding model 'Test5Block'
        db.create_table(u'multi_table_test5block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test5Block'])

        # Adding model 'Test15Block'
        db.create_table(u'multi_table_test15block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test15Block'])

        # Adding model 'Test13Block'
        db.create_table(u'multi_table_test13block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test13Block'])

        # Adding model 'Test4Block'
        db.create_table(u'multi_table_test4block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test4Block'])

        # Adding model 'Test11Block'
        db.create_table(u'multi_table_test11block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test11Block'])

        # Adding model 'Test14Block'
        db.create_table(u'multi_table_test14block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test14Block'])

        # Adding model 'Test8Block'
        db.create_table(u'multi_table_test8block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test8Block'])

        # Adding model 'Test16Block'
        db.create_table(u'multi_table_test16block', (
            (u'contentblock_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['multi_table.ContentBlock'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('multi_table', ['Test16Block'])


    def backwards(self, orm):
        # Deleting model 'Test7Block'
        db.delete_table(u'multi_table_test7block')

        # Deleting model 'Test17Block'
        db.delete_table(u'multi_table_test17block')

        # Deleting model 'Test1Block'
        db.delete_table(u'multi_table_test1block')

        # Deleting model 'Test9Block'
        db.delete_table(u'multi_table_test9block')

        # Deleting model 'Test10Block'
        db.delete_table(u'multi_table_test10block')

        # Deleting model 'Test6Block'
        db.delete_table(u'multi_table_test6block')

        # Deleting model 'Test3Block'
        db.delete_table(u'multi_table_test3block')

        # Deleting model 'Test0Block'
        db.delete_table(u'multi_table_test0block')

        # Deleting model 'Test19Block'
        db.delete_table(u'multi_table_test19block')

        # Deleting model 'Test2Block'
        db.delete_table(u'multi_table_test2block')

        # Deleting model 'Test12Block'
        db.delete_table(u'multi_table_test12block')

        # Deleting model 'Test18Block'
        db.delete_table(u'multi_table_test18block')

        # Deleting model 'Test5Block'
        db.delete_table(u'multi_table_test5block')

        # Deleting model 'Test15Block'
        db.delete_table(u'multi_table_test15block')

        # Deleting model 'Test13Block'
        db.delete_table(u'multi_table_test13block')

        # Deleting model 'Test4Block'
        db.delete_table(u'multi_table_test4block')

        # Deleting model 'Test11Block'
        db.delete_table(u'multi_table_test11block')

        # Deleting model 'Test14Block'
        db.delete_table(u'multi_table_test14block')

        # Deleting model 'Test8Block'
        db.delete_table(u'multi_table_test8block')

        # Deleting model 'Test16Block'
        db.delete_table(u'multi_table_test16block')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'multi_table.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'multi_table.contentblock': {
            'Meta': {'object_name': 'ContentBlock'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blocks'", 'to': u"orm['multi_table.Container']"}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'multi_table.imageblock': {
            'Meta': {'object_name': 'ImageBlock', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'multi_table.test0block': {
            'Meta': {'object_name': 'Test0Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test10block': {
            'Meta': {'object_name': 'Test10Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test11block': {
            'Meta': {'object_name': 'Test11Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test12block': {
            'Meta': {'object_name': 'Test12Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test13block': {
            'Meta': {'object_name': 'Test13Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test14block': {
            'Meta': {'object_name': 'Test14Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test15block': {
            'Meta': {'object_name': 'Test15Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test16block': {
            'Meta': {'object_name': 'Test16Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test17block': {
            'Meta': {'object_name': 'Test17Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test18block': {
            'Meta': {'object_name': 'Test18Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test19block': {
            'Meta': {'object_name': 'Test19Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test1block': {
            'Meta': {'object_name': 'Test1Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test2block': {
            'Meta': {'object_name': 'Test2Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test3block': {
            'Meta': {'object_name': 'Test3Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test4block': {
            'Meta': {'object_name': 'Test4Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test5block': {
            'Meta': {'object_name': 'Test5Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test6block': {
            'Meta': {'object_name': 'Test6Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test7block': {
            'Meta': {'object_name': 'Test7Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test8block': {
            'Meta': {'object_name': 'Test8Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'multi_table.test9block': {
            'Meta': {'object_name': 'Test9Block', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'multi_table.textblock': {
            'Meta': {'object_name': 'TextBlock', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'multi_table.userblock': {
            'Meta': {'object_name': 'UserBlock', '_ormbases': [u'multi_table.ContentBlock']},
            u'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['multi_table.ContentBlock']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['multi_table']