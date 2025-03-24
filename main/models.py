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


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    slug = models.SlugField(verbose_name='Слаг', help_text='Данное поле заполняется автоматически')
    preview = models.ImageField(verbose_name='Заставка', upload_to='products/preview/', null=True, blank=True)
    description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    barcode = models.CharField(verbose_name='Штрих код', max_length=100)
    price = models.IntegerField(verbose_name='Цена', default=0)
    in_stock = models.BooleanField(verbose_name='В наличии?', default=True)
    category = models.ManyToManyField(Category, null=True, verbose_name='Категория')
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='Серия', null=True)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, verbose_name='Издательство',
                                         null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
