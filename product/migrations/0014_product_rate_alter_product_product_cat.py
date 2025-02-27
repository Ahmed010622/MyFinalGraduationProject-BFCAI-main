# Generated by Django 4.1.6 on 2023-03-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_auto_20230306_2015"),
    ]

    operations = [
        migrations.AddField(
            model_name="product", name="rate", field=models.IntegerField(default=0),
        ),
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
                    ("Men-Black t-shirt", "Men-Black t-shirt"),
                    ("Men-White t-shirt", "Men-White t-shirt"),
                    ("Men-Blue t-shirt", "Men-Blue t-shirt"),
                    ("Men-Red t-shirt", "Men-Red t-shirt"),
                    ("Men-Green t-shirt", "Men-Green t-shirt"),
                    ("Women-dress-white", "Women-dress-white"),
                    ("Women-dress-red", "Women-dress-red"),
                    ("Women-dress-blue", "Women-dress-blue"),
                    ("Hat-black", "Hat-black"),
                    ("Hat-white", "Hat-white"),
                    ("Hat-blue", "Hat-blue"),
                    ("Hat-red", "Hat-red"),
                    ("Hat-green", "Hat-green"),
                    ("Black-jeans", "Black-jeans"),
                    ("White-jeans", "White-jeans"),
                    ("Black-shoes", "Black-shoes"),
                    ("White-shoes", "White-shoes"),
                    ("Blue-shoes", "Blue-shoes"),
                    ("Red-shoes", "Red-shoes"),
                    ("Green-shoes", "Green-shoes"),
                    ("Black-sweater", "Black-sweater"),
                    ("White-sweater", "White-sweater"),
                    ("Blue-sweater", "Blue-sweater"),
                    ("Red-sweater", "Red-sweater"),
                    ("Black-jacket", "Black-jacket"),
                    ("White-jacket", "White-jacket"),
                    ("Blue-jacket", "Blue-jacket"),
                    ("Red-jacket", "Red-jacket"),
                ],
                max_length=100,
            ),
        ),
    ]
