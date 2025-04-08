from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]


class Subcategory(models.Model):
    name = models.CharField(max_length=150, verbose_name="Подкатегория")
    slug = models.SlugField(
        max_length=150,
        verbose_name="Короткая ссылка",
        help_text="Данное поле заполнять не нужно!",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="subcategories",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ["-created_at"]


# class ProductVariant(models.Model):
#     name = models.CharField(max_length=200, verbose_name='Вид продукта')
#     slug = models.SlugField(verbose_name='Короткая ссылка на продукт', help_text='Данное поле заполнять не нужно')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
#                                  related_name='product_variants')
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='product_variants',
#                                     verbose_name='Подкатегория')
#
#     created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(ProductVariant, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Вид продукта'
#         verbose_name_plural = 'Виды продуктов'
#         ordering = ['-created_at']


class PublishingHouse(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(
        verbose_name="Короткая ссылка", help_text="Данное поле заполнять не нужно!"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class CategoryAge(models.Model):
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return f"{self.age}"

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возрастa"


class ProductBaseCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Короткая ссылка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Базовая категория"
        verbose_name_plural = "Базовые категории"


class Product(models.Model):
    barcode = models.IntegerField(verbose_name="Штрихкод", unique=True)
    title = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Короткая ссылка")
    preview = models.ImageField(
        upload_to="products/", null=True, blank=True, verbose_name="Заставка"
    )
    price = models.FloatField(verbose_name="Цена")
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    sku = models.CharField(max_length=200, verbose_name="Артикул")
    ages = models.ManyToManyField(CategoryAge, verbose_name="Возраста")
    size = models.CharField(
        verbose_name="Размер", max_length=200, null=True, blank=True
    )
    publisher = models.ForeignKey(
        PublishingHouse,
        on_delete=models.CASCADE,
        verbose_name="Издательство",
        related_name="products",
    )
    product_code = models.IntegerField(verbose_name="Код товара", default=0)
    main_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Основная категория",
        related_name="products",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
        related_name="products",
    )
    base_category = models.ManyToManyField(
        ProductBaseCategory,
        verbose_name="Базовые категории",
        related_name="products",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="images",
    )
    image = models.ImageField(
        verbose_name="Фотография", upload_to="products/gallery/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продукта"
