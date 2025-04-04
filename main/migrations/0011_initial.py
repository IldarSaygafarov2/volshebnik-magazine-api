# Generated by Django 5.1.7 on 2025-03-31 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0010_remove_category_catalog_remove_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Категория')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Подкатегория')),
                ('slug', models.SlugField(help_text='Данное поле заполнять не нужно!', max_length=150, unique=True, verbose_name='Короткая ссылка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Вид продукта')),
                ('slug', models.SlugField(help_text='Данное поле заполнять не нужно', unique=True, verbose_name='Короткая ссылка на продукт')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='main.category', verbose_name='Категория')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='main.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Вид продукта',
                'verbose_name_plural': 'Виды продуктов',
                'ordering': ['-created_at'],
            },
        ),
    ]
