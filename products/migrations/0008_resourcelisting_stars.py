# Generated by Django 5.0.1 on 2024-04-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_resourcelisting_admin_approval"),
    ]

    operations = [
        migrations.AddField(
            model_name="resourcelisting",
            name="stars",
            field=models.IntegerField(default=0),
        ),
    ]
