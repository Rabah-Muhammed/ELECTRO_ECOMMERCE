# Generated by Django 5.0.6 on 2024-06-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_images2_product_images3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images3',
        ),
    ]
