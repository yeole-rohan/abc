# Generated by Django 3.1.4 on 2021-03-13 14:35

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_gp', models.BooleanField(default=False)),
                ('is_observar', models.BooleanField(default=False)),
                ('is_s2', models.BooleanField(default=False)),
                ('is_ceo', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('phaseno', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Confirmation',
                'verbose_name_plural': 'Confirmations',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.user', verbose_name='CEO')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('username', models.TextField()),
            ],
            options={
                'verbose_name': 'CEO',
                'verbose_name_plural': 'CEO',
            },
        ),
        migrations.CreateModel(
            name='Grampanchayat',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.user', verbose_name='GP')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('gram_sevak', 'Gram Sevak'), ('gram_vikas_adhikari', 'Gram Vikas Adhikari')], max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.", regex='^\\d{10,10}$')])),
                ('date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('username', models.TextField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.district')),
            ],
            options={
                'verbose_name': 'Grampanchayat',
                'verbose_name_plural': 'Grampanchayats',
            },
        ),
        migrations.CreateModel(
            name='Observar',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.user', verbose_name='observar')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('username', models.TextField()),
            ],
            options={
                'verbose_name': 'Observar',
                'verbose_name_plural': 'Observars',
            },
        ),
        migrations.CreateModel(
            name='S2',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.user', verbose_name='account')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('username', models.TextField(default='ac')),
            ],
            options={
                'verbose_name': 'S2',
                'verbose_name_plural': 'S2S',
            },
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taluka', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.district')),
            ],
        ),
        migrations.CreateModel(
            name='Panchayat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panchayat', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='ServilencePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('phoseno', models.PositiveSmallIntegerField()),
                ('utrno', models.PositiveIntegerField()),
                ('remark', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('matched', 'Matched'), ('unmatched', 'Unmatched')], max_length=1000)),
                ('user', models.ManyToManyField(to='portal.Grampanchayat', verbose_name='Grampanchayat ServilencePayment')),
            ],
            options={
                'verbose_name': 'ServilencePayment',
                'verbose_name_plural': 'ServilencePayments',
            },
        ),
        migrations.CreateModel(
            name='Servilence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('document', models.ImageField(upload_to='document/')),
                ('phoseno', models.PositiveSmallIntegerField()),
                ('user', models.ManyToManyField(to='portal.Grampanchayat', verbose_name='Grampanchayat Servilence')),
            ],
            options={
                'verbose_name': 'Servilence',
                'verbose_name_plural': 'Servilences',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('utrno', models.PositiveIntegerField()),
                ('remark', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('matched', 'Matched'), ('unmatched', 'Unmatched')], max_length=1000)),
                ('confirmation', models.ManyToManyField(to='portal.Confirmation', verbose_name='Confirmation to payment')),
                ('user', models.ManyToManyField(to='portal.Grampanchayat', verbose_name='Grampanchayat Payment')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AddField(
            model_name='grampanchayat',
            name='panchayat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.panchayat'),
        ),
        migrations.AddField(
            model_name='grampanchayat',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.taluka'),
        ),
        migrations.AddField(
            model_name='confirmation',
            name='user',
            field=models.ManyToManyField(to='portal.Grampanchayat', verbose_name='Grampanchayat Confirmation'),
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('document', models.ImageField(upload_to='document/')),
                ('phoseno', models.PositiveSmallIntegerField()),
                ('user', models.ManyToManyField(to='portal.Grampanchayat', verbose_name='Grampanchayat Audit')),
            ],
            options={
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
            },
        ),
    ]