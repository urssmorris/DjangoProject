# Generated by Django 3.1.5 on 2021-07-09 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210708_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watched',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='watched',
            field=models.ManyToManyField(related_name='watchlist_btn', to=settings.AUTH_USER_MODEL),
        ),
    ]