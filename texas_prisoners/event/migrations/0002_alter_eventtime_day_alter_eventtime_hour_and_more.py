# Generated by Django 4.1.6 on 2023-02-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventtime", name="day", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="eventtime", name="hour", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="eventtime", name="minute", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="eventtime", name="month", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="eventtime", name="second", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="eventtime", name="year", field=models.IntegerField(null=True),
        ),
    ]
