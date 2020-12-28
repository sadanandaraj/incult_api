# Generated by Django 2.2.5 on 2020-12-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='lists', to='products.Product'),
        ),
    ]
