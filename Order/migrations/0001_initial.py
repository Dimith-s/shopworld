# Generated by Django 5.0.6 on 2024-07-16 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(3, 'order_confirmed'), (2, 'order_processed'), (4, 'order_rejected')], default='CART_STAGE')),
                ('total_price', models.FloatField(default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordered', to='customer.customers')),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_carts', to='Product.products')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_items', to='Order.orders')),
            ],
        ),
    ]
