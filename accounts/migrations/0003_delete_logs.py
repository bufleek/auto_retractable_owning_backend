# Generated by Django 4.1.3 on 2022-11-22 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_logs"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Logs",
        ),
    ]