# Generated by Django 5.1.2 on 2024-11-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_rename_shipping_province_shippingaddress_shipping_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shipping_state',
            new_name='shipping_province',
        ),
    ]
