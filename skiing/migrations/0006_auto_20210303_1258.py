# Generated by Django 3.1.7 on 2021-03-03 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skiing", "0005_auto_20210303_1239"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_professional_skier",
        ),
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="skiing.skiliftlimit",
            ),
            preserve_default=False,
        ),
    ]