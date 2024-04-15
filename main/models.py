from django.db import models
from django.core.validators import RegexValidator


class Number(models.Model):
    class Meta:
        abstract = True

    cadastral_number = models.CharField(
        verbose_name="Кадастровый номер",
        max_length=20,
        validators=[
            RegexValidator(
                regex="^[0-9\:]",
                message='Это поле может содержать кадастровый номер в формате "22:22:123555:215"',
                code="invalid_symbols",
            )
        ],
    )


class NumberHistory(Number):
    pass


class Query(Number):
    latitude = models.CharField(
        verbose_name="Широта",
        max_length=10,
        validators=[
            RegexValidator(
                regex="^[0-9\.]",
                message='Это поле может содержать координату в формате "22.15"',
                code="invalid_symbols",
            )
        ],
    )
    longitude = models.CharField(
        verbose_name="Долгота",
        max_length=10,
        validators=[
            RegexValidator(
                regex="^[0-9\.]",
                message='Это поле может содержать координату в формате "22.15"',
                code="invalid_symbols",
            )
        ],
    )
    result = models.BooleanField(verbose_name="Результат запроса")
    create_at = models.DateTimeField(verbose_name="Создано", auto_now=True)

    def __str__(self):
        return f"Кадастровый номер: {self.cadastral_number} - Широта: {self.latitude} - Долгота: {self.longitude} - Результат запроса: {self.result}"
