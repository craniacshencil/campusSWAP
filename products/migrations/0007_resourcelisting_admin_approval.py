# Generated by Django 5.0.1 on 2024-03-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_resourcelisting"),
    ]

    operations = [
        migrations.AddField(
            model_name="resourcelisting",
            name="admin_approval",
            field=models.CharField(default=False, max_length=5),
            preserve_default=False,
        ),
    ]
