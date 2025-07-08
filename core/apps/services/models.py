from django.db import models

class Service(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150, unique=True)
    is_visible = models.BooleanField(verbose_name='Сделать видимой на главной странице?', default=True)
    description = models.TextField(verbose_name='Описание')
    icon = models.ImageField(verbose_name='Иконка', upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
