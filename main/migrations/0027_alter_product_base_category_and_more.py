# Generated by Django 5.1.7 on 2025-04-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_product_binding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='base_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='main.productbasecategory', verbose_name='Базовые категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Код товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название'),
        ),
    ]
