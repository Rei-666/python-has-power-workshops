# Generated by Django 3.1.7 on 2021-03-03 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skiing", "0006_auto_20210303_1258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="skiing.skiliftlimit",
            ),
        ),
    ]
