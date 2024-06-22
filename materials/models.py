from django.db import models


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
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )

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
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lesson_set",
        verbose_name="Курс",
        help_text="Выберите курс",
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}, курс - {self.course}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
