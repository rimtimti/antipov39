from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("ping/", views.ping, name="ping"),
    path("query/", views.query, name="query"),
    path("history/", views.history, name="history"),
    path("result/", views.result, name="result"),
    path("history_of_number/", views.history_of_number, name="history_of_number"),
]
