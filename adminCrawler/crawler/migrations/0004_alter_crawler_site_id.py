# Generated by Django 4.2.1 on 2023-07-15 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0003_alter_crawler_options_alter_crawler_errors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crawler",
            name="site_id",
            field=models.ForeignKey(
                db_column="site_id",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="crawler.site",
            ),
        ),
    ]
