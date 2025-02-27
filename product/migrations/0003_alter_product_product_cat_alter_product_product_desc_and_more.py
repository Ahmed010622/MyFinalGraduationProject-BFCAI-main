# Generated by Django 4.1.6 on 2023-02-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_options_product_product_image2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_cat",
            field=models.CharField(
                choices=[
                    ("Fashion-Accessories", "Fashion-Accessories"),
                    ("men-s-clothing", "men-s-clothing"),
                    ("women-s-clothing", "women-s-clothing"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_desc",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_price",
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity_avaliable",
            field=models.CharField(max_length=100),
        ),
    ]
