# Generated by Django 3.1.5 on 2021-07-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to='auction/images/'),
        ),
    ]
