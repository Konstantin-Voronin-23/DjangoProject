from django.db import models
from django.utils import timezone


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )

    preview = models.ImageField(
        upload_to="blogs/previews/",
        null=True,
        blank=True,
        verbose_name="Превью",
        help_text="Загрузите превью-изображение",
    )

    content = models.TextField(
        verbose_name='Содержимое'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата публикации'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='Статус'
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров'
    )

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        elif self.status == 'draft':
            self.published_at = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['-created_at']