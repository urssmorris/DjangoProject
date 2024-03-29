# Generated by Django 3.1.5 on 2021-07-08 21:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210705_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='watchlist',
            field=models.ManyToManyField(related_name='watchlist_btn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10, verbose_name='Bid'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('a', 'Microprocessors'), ('b', 'Motherboards'), ('c', 'Computer Memory (RAM)'), ('d', 'Hard Disk Drives'), ('e', 'Computer Case'), ('f', 'Monitors'), ('g', 'Periferics'), ('h', 'Others')], default='a', max_length=1),
        ),
    ]
