# Generated by Django 5.1.7 on 2025-04-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_product_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pages',
            field=models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='количество страниц'),
        ),
    ]
