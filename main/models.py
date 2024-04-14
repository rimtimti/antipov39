from django.db import models
from django.core.validators import RegexValidator


class Number(models.Model):
    class Meta:
        abstract = True

    cadastral_number = models.CharField(
        verbose_name="Кадастровый номер",
        validators=[
            RegexValidator(
                regex="^[0-9\:]",
                message='Это поле может содержать только кадастровый номер в формате "22:22:123555:215"',
                code="invalid_symbols",
            )
        ],
        max_length=20,
    )


class NumberHistory(Number):
    pass


class Query(Number):
    latitude = models.CharField(verbose_name="Широта", max_length=10)
    longitude = models.CharField(verbose_name="Долгота", max_length=10)
    result = models.BooleanField(verbose_name="Результат запроса")
    create_at = models.DateTimeField(verbose_name="Создано", auto_now=True)
