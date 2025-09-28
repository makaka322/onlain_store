from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Заголовок", help_text="Введите название Заголовка"
    )
    content = models.TextField(
        verbose_name="Содержимое публикации", blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="photo_blog/", verbose_name="Изображение", blank=True, null=True
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    def __str__(self):
        return f'{self.title} создано: {self.created_at}, количество просмотров: {self.views_counter}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['title']
