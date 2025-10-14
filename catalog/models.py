from django.db import models
from users.models import User

class Category(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(
        max_length=100, verbose_name="Товар", help_text="Введите название товара"
    )
    description = models.TextField(
        verbose_name="Описание товара",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    photo_product = models.ImageField(
        upload_to="photos/", verbose_name="Изображение", blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Укажите цену за покупку товара",
        default=0,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )

    is_published = models.BooleanField(
        default=False, verbose_name="Статус публикации")

    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.name}, относится к категории {self.category}, цена: {self.price}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category", "price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
