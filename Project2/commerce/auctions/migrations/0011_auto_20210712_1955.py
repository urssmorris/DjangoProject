# Generated by Django 3.1.5 on 2021-07-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210712_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
