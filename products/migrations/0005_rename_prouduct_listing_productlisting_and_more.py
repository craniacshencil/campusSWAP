# Generated by Django 5.0.1 on 2024-03-25 13:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_remove_prouduct_listing_listing_published"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Prouduct_listing",
            new_name="ProductListing",
        ),
        migrations.AlterModelTable(
            name="productlisting",
            table="product_listings",
        ),
    ]
