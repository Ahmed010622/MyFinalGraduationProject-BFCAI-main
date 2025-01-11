# Generated by Django 4.1.6 on 2023-02-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_remove_product_quantity_available"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="product_image2",),
        migrations.RemoveField(model_name="product", name="product_image3",),
        migrations.AddField(
            model_name="product",
            name="quantity_available",
            field=models.CharField(default="Not Available right now!", max_length=100),
        ),
    ]
