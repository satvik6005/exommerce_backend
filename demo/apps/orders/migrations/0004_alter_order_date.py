# Generated by Django 4.2.5 on 2023-10-04 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_alter_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 4, 10, 17, 47, 975825, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
