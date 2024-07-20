# Generated by Django 5.0.6 on 2024-07-06 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keen_app', '0004_remove_product_color_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagevarient',
            name='p_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='keen_app.product'),
        ),
    ]