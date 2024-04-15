from django.contrib import admin

from main.models import Query


class QueryAdmin(admin.ModelAdmin):
    """Список запросов"""

    list_display = [
        "cadastral_number",
        "latitude",
        "longitude",
        "result",
        "create_at",
    ]

    fieldsets = [
        (
            "Кадастровый номер",
            {
                "description": "Кадастровый номер",
                "fields": ["cadastral_number"],
            },
        ),
        (
            "latitude",
            {
                "description": "Широта",
                "fields": ["latitude"],
            },
        ),
        (
            "longitude",
            {
                "description": "Долгота",
                "fields": ["longitude"],
            },
        ),
        (
            "result",
            {
                "description": "Результат запроса",
                "fields": ["result"],
            },
        ),
    ]


# Register your models here.
admin.site.register(Query, QueryAdmin)
