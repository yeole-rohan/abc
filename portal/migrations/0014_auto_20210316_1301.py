# Generated by Django 3.1.4 on 2021-03-16 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20210316_0913'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Servilence',
            new_name='ServilenceAudit',
        ),
    ]