# Generated by Django 4.1.6 on 2023-02-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_remove_product_product_image2_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Material",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Cotton", "Cotton"),
                            ("Polyester", "Polyester"),
                            ("Silk", "Silk"),
                            ("Wool", "Wool"),
                            ("Leather", "Leather"),
                            ("Fur", "Fur"),
                            ("Linen", "Linen"),
                            ("Rayon", "Rayon"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Materials",},
        ),
        migrations.RemoveField(model_name="product", name="product_desc",),
        migrations.AlterField(
            model_name="product",
            name="product_cat",
            field=models.CharField(
                choices=[
                    ("Fashion-Accessories", "Fashion-Accessories"),
                    ("men-s-clothing", "men-s-clothing"),
                    ("women-s-clothing", "women-s-clothing"),
                    ("Kids", "Kids"),
                    ("Home", "Home"),
                ],
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_material",
            field=models.ManyToManyField(to="product.material"),
        ),
    ]
