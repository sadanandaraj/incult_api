# Generated by Django 2.2.5 on 2020-12-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='store_logo')),
                ('description', models.TextField()),
                ('offer', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=140)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('close', 'Close')], max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'store Type',
                'ordering': ['created'],
            },
        ),
    ]
