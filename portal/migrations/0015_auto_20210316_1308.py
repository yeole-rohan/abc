# Generated by Django 3.1.4 on 2021-03-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20210316_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servilenceaudit',
            name='document',
            field=models.FileField(upload_to='document/'),
        ),
    ]
