# Generated by Django 5.0.6 on 2024-07-06 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keen_app', '0003_remove_imagevarient_product_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
        migrations.AddField(
            model_name='imagevarient',
            name='p_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='keen_app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
