# Generated by Django 5.0.6 on 2024-07-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_delete_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
    ]
