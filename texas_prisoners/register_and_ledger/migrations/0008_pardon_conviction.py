# Generated by Django 4.1.5 on 2023-01-30 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_and_ledger', '0007_conviction_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pardon',
            name='conviction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pardon', to='register_and_ledger.conviction'),
        ),
    ]
