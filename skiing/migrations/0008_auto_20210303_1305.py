# Generated by Django 3.1.7 on 2021-03-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skiing", "0007_auto_20210303_1303"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="partnered_ski_resorts",
            field=models.ManyToManyField(null=True, to="skiing.SkiResort"),
        ),
    ]
