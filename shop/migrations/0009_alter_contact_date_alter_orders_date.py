# Generated by Django 4.0 on 2022-02-04 10:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_contact_date_alter_orders_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 4, 10, 1, 26, 690609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 4, 10, 1, 26, 691609, tzinfo=utc)),
        ),
    ]
