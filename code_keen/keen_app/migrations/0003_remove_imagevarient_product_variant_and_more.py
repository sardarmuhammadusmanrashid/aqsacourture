# Generated by Django 5.0.6 on 2024-07-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keen_app', '0002_remove_product_category_remove_product_color_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagevarient',
            name='product_variant',
        ),
        migrations.AddField(
            model_name='product',
            name='img_variant',
            field=models.ManyToManyField(to='keen_app.imagevarient'),
        ),
    ]