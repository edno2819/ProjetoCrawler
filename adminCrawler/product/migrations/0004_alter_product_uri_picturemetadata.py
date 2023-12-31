# Generated by Django 4.2.1 on 2023-07-16 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_product_category_alter_product_site_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="uri",
            field=models.URLField(max_length=255),
        ),
        migrations.CreateModel(
            name="PictureMetadata",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("picture_url", models.URLField(max_length=512)),
                ("metadata", models.JSONField(blank=True, max_length=1024, null=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        db_column="product_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "db_table": "pictures_metadata",
            },
        ),
    ]
