# Generated by Django 3.1.5 on 2021-07-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210712_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='commerce/auctions/static/auctions/images/default.jpg', upload_to='auction/images/'),
        ),
    ]
