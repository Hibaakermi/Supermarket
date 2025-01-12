# Generated by Django 5.1.4 on 2024-12-06 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "marketAdmin",
            "0002_grocrey_gamm_vegitables_vamm_alter_grocrey_gimg_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
