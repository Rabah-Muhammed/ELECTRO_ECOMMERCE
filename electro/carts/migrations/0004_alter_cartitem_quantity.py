# Generated by Django 5.0.6 on 2024-07-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='Quantity',
            field=models.IntegerField(default=1),
        ),
    ]
