# Generated by Django 3.1.4 on 2021-03-16 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20210316_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servilencepayment',
            old_name='phoseno',
            new_name='phaseno',
        ),
    ]
