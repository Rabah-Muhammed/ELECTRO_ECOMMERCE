# Generated by Django 5.0.6 on 2024-07-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0026_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
