# Generated by Django 3.2.16 on 2022-11-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("status", "0003_alter_statuschoices_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="created_at",
            field=models.DateTimeField(),
        ),
    ]
