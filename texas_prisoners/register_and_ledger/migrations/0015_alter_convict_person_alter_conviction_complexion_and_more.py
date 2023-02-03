# Generated by Django 4.1.6 on 2023-02-03 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("place", "0002_alter_place_bounds_alter_place_latitude_and_more"),
        ("event", "0003_alter_eventtime_day_alter_eventtime_hour_and_more"),
        ("person", "0002_alter_person_name"),
        ("register_and_ledger", "0014_alter_death_cause"),
    ]

    operations = [
        migrations.AlterField(
            model_name="convict",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.convict",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="complexion",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.racialcategory",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conviction",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="expires",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conviction_expires",
                to="event.eventtime",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="marital_relations",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.maritalcategory",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="occupation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conviction",
                to="register_and_ledger.occupationalcategory",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="offence",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.offencecategory",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="pardons",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="parents",
                to="register_and_ledger.pardon",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="place",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conviction_place",
                to="place.place",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="place_of_residence",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="residence",
                to="place.place",
            ),
        ),
        migrations.AlterField(
            model_name="conviction",
            name="time",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conviction_time",
                to="event.eventtime",
            ),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="birth",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.birth",
            ),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="convict_numer",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="death",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.death",
            ),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="person.person",
            ),
        ),
        migrations.AlterField(
            model_name="convictrecord",
            name="record_date",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="event.eventtime",
            ),
        ),
        migrations.AlterField(
            model_name="escape",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="escape",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="escape",
            name="recaptured",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="escape",
            name="returned",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="escape",
            name="same_day",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="escape",
            name="surrender",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="escape",
            name="trusty",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="escape",
            name="wounded",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="hospitalization",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hospitalization",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="convict",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="convict_lease",
                to="register_and_ledger.convict",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lease",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="end_date",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lease_end_date",
                to="event.eventtime",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="lessee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessee_lease",
                to="register_and_ledger.company",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="start_date",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lease_start_date",
                to="event.eventtime",
            ),
        ),
        migrations.AlterField(
            model_name="lease",
            name="where_after",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="place.place",
            ),
        ),
        migrations.AlterField(
            model_name="pardon",
            name="conviction",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pardon",
                to="register_and_ledger.conviction",
            ),
        ),
        migrations.AlterField(
            model_name="pardon",
            name="pardoner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pardon",
                to="person.person",
            ),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="punishment",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="duration_in_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="lessee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="person.person",
            ),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="method",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="punishment_method",
                to="register_and_ledger.punishmentmethod",
            ),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="prison",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="punishment_prison",
                to="place.place",
            ),
        ),
        migrations.AlterField(
            model_name="punishment",
            name="reason",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="punishmentmethod",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="return",
            name="new_conviction",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="return",
            name="new_term",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="return",
            name="number",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="return",
            name="parole_violation",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="transfer",
            name="number",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="workforprison",
            name="convict_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="work_for_prison",
                to="register_and_ledger.convictrecord",
            ),
        ),
        migrations.AlterField(
            model_name="workforprison",
            name="work_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="register_and_ledger.worktype",
            ),
        ),
    ]
