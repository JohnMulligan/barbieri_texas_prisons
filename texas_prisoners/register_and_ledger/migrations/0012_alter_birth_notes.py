# Generated by Django 4.1.6 on 2023-02-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "register_and_ledger",
            "0011_alter_birth_date_time_alter_birth_place_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="birth",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
