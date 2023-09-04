# Generated by Django 4.2.4 on 2023-08-17 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_delete_payment_order_secret_key_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order',
            name='quantity',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 52, 0, 214152, tzinfo=datetime.timezone.utc)),
        ),
    ]