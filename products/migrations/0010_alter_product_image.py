# Generated by Django 5.2 on 2025-06-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
