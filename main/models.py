from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    icon = models.FileField(verbose_name='Иконка', upload_to='catalogs/icons/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'



class Category(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, help_text='Данное поле заполняется автоматически')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PublishingHouse(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.SlugField(unique=True, help_text='Данное поле заполняется автоматически')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Series(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.SlugField(unique=True, help_text='Данное поле заполняется автоматически')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'