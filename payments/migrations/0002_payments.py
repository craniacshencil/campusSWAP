# Generated by Django 5.0.1 on 2024-04-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buyer_moodleID", models.IntegerField()),
                ("seller_moodleID", models.IntegerField()),
                ("orderID", models.CharField(max_length=100)),
                ("paymentID", models.CharField(max_length=100)),
                ("transaction_signature", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "payments",
            },
        ),
    ]
