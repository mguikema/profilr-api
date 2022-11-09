# Generated by Django 3.2.16 on 2022-11-09 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0002_buurt_gemeente_wijk"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="buurt",
            options={
                "ordering": ["_type", "code"],
                "verbose_name": "Buurt",
                "verbose_name_plural": "Buurten",
            },
        ),
        migrations.AlterModelOptions(
            name="gemeente",
            options={
                "ordering": ["_type", "code"],
                "verbose_name": "Gemeente",
                "verbose_name_plural": "Gemeentes",
            },
        ),
        migrations.AlterModelOptions(
            name="wijk",
            options={
                "ordering": ["_type", "code"],
                "verbose_name": "Wijk",
                "verbose_name_plural": "Wijken",
            },
        ),
        migrations.AlterUniqueTogether(
            name="buurt",
            unique_together={("code", "_type")},
        ),
        migrations.AlterUniqueTogether(
            name="gemeente",
            unique_together={("code", "_type")},
        ),
        migrations.AlterUniqueTogether(
            name="wijk",
            unique_together={("code", "_type")},
        ),
    ]
