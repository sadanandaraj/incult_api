# Generated by Django 2.2.5 on 2020-12-14 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='follower',
            field=models.ManyToManyField(blank=True, null=True, related_name='store_follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='storeType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='stores.StoreType'),
        ),
    ]
