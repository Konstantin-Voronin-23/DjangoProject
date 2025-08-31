from django.db import models
from users.models import User


class Product(models.Model):
    """Класс для описания продуктов"""

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product/image",
        null=True,
        blank=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Наименование категории продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Стоимость продукта", help_text="Введите стоимость продукта"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания продукта"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения продукта"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_products',
        verbose_name='Продукт пользователя')

    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Указывает, опубликован ли товар на сайте. По умолчанию — не опубликован.",
    )

    def __str__(self):
        """Метод для отображения информации пользователю"""

        return f"{self.name} {self.category}"

    class Meta:
        """ Класс отображения метаданных"""

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
            "price",
        ]
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]


class Category(models.Model):
    """Класс для описания категорий"""

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание"
    )

    def __str__(self):
        """Метод для отображения информации пользователю"""

        return self.name

    class Meta:
        """ Класс отображения метаданных"""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]
