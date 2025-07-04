from django.db import models

class NewsPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(verbose_name='Короткая ссылка', help_text='Данное поле заполнять не нужно')
    content = models.TextField(verbose_name='описание')
    preview = models.ImageField(verbose_name='фото', upload_to='news/', null=True, blank=True,
                                default='placeholder.jpg')
    is_visible = models.BooleanField(verbose_name='Показывать на главной стронице?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

