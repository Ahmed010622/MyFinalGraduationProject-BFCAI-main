# Generated by Django 4.1.2 on 2023-05-20 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("review_blog", "0010_comment_user_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="NLPReviewStored",
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
                ("sentiment", models.CharField(max_length=300)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nlp_reviews",
                        to="review_blog.review",
                    ),
                ),
            ],
            options={"ordering": ["-review"],},
        ),
    ]
