# Generated by Django 5.0.1 on 2024-03-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="prouduct_listing",
            name="admin_approval",
            field=models.CharField(default="false", max_length=5),
            preserve_default=False,
        ),
    ]
