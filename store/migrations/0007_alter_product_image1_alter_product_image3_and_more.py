# Generated by Django 5.1.2 on 2024-12-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image7',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image8',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
    ]
