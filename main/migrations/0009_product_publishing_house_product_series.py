# Generated by Django 5.1.7 on 2025-03-24 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publishing_house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.publishinghouse', verbose_name='Издательство'),
        ),
        migrations.AddField(
            model_name='product',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.series', verbose_name='Серия'),
        ),
    ]
