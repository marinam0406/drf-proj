# Generated by Django 5.0.6 on 2024-06-24 19:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото профиля",
                null=True,
                upload_to="users/avatars",
                verbose_name="Аватар",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите город",
                max_length=35,
                null=True,
                verbose_name="Город",
            ),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты"),
                ),
                ("total_sum", models.FloatField(verbose_name="Сумма оплаты")),
                (
                    "payment_method",
                    models.CharField(max_length=20, verbose_name="Способ оплаты"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="Лекция",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]