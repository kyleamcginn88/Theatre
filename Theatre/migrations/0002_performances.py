# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Theatre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=[b'%Y-%m-%d'])),
                ('name', models.CharField(max_length=254)),
                ('genre', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
