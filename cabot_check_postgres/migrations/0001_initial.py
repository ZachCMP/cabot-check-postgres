# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 11:44
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabotapp', '0006_auto_20170821_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostgresStatusCheck',
            fields=[
                ('statuscheck_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cabotapp.StatusCheck')),
                ('host', models.TextField(help_text=b'Postgres host', null=True)),
                ('port', models.PositiveIntegerField(help_text=b'Postgres port', null=True)),
                ('dbname', models.TextField(help_text=b'Postgres database name', null=True)),
                ('dbuser', models.TextField(help_text=b'Postgres user', null=True)),
                ('dbpassword', models.TextField(help_text=b'Postgres password', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.statuscheck',),
        ),
    ]
