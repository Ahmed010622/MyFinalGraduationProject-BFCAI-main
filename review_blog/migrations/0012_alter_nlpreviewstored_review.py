# Generated by Django 4.1.2 on 2023-05-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review_blog", "0011_nlpreviewstored"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nlpreviewstored",
            name="review",
            field=models.CharField(max_length=800),
        ),
    ]
