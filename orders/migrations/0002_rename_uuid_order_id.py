# Generated by Django 4.2.7 on 2023-11-28 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="uuid",
            new_name="id",
        ),
    ]
