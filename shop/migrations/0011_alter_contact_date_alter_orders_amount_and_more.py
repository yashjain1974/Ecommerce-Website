# Generated by Django 4.0 on 2022-02-04 16:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders_amount_alter_contact_date_alter_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 4, 16, 17, 37, 520365, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 4, 16, 17, 37, 520365, tzinfo=utc)),
        ),
    ]
