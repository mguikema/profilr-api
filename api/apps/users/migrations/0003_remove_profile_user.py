# Generated by Django 3.2.16 on 2023-01-09 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_filters"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
    ]
