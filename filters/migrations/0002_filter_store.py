# Generated by Django 2.2.5 on 2020-12-14 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='stores.Store'),
        ),
    ]
