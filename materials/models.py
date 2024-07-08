from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    image = models.ImageField(
        upload_to="materials/course",
        verbose_name="Превью(картинка)",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание курса",
        **NULLABLE
    )
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        **NULLABLE
    )
    amount = models.PositiveIntegerField(verbose_name='стоимость курса', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    image = models.ImageField(
        upload_to="materials/lesson",
        verbose_name="Превью(картинка)",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание урока", **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lesson_set",
        verbose_name="Курс",
        help_text="Выберите курс",
    )
    url = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец',
                              **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='стоимость курса', **NULLABLE)

    def __str__(self):
        return f"{self.name}, курс - {self.course}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Subscription(models.Model):
    """Model for subscription"""

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Выберите пользователя",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
