# Generated by Django 5.1.7 on 2025-03-31 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_publishing_house_product_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catalog',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='publishing_house',
        ),
        migrations.RemoveField(
            model_name='product',
            name='series',
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='PublishingHouse',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Series',
        ),
    ]
