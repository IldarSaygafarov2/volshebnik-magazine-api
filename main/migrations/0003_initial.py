# Generated by Django 5.1.7 on 2025-03-22 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_remove_subcategory_category_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('icon', models.FileField(blank=True, null=True, upload_to='catalogs/icons/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Данное поле заполняется автоматически', unique=True)),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Данное поле заполняется автоматически', unique=True)),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Данное поле заполняется автоматически', unique=True)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catalog', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
