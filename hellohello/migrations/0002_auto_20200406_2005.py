# Generated by Django 3.0.2 on 2020-04-06 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellohello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 20, 5, 33, 863192), verbose_name='DATE'),
        ),
        migrations.AlterField(
            model_name='updateorder',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 20, 5, 33, 863192), verbose_name='DATE'),
        ),
    ]
