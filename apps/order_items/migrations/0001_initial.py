# Generated by Django 5.0.6 on 2024-10-17 02:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Quantity')),
                ('creat_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Creation Date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_order', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realated_order_item_product', to='products.product')),
            ],
            options={
                'db_table': 'order_time',
            },
        ),
    ]