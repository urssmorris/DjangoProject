# Generated by Django 3.1.5 on 2021-07-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210709_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='auction/images/'),
        ),
    ]