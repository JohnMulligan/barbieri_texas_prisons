# Generated by Django 4.1.5 on 2023-01-30 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_and_ledger', '0006_hospitalization_convict_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='conviction',
            name='occupation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conviction', to='register_and_ledger.occupationalcategory'),
        ),
    ]
