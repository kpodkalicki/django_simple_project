# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20170330_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='level',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='notes.Topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]
