import random
import time
from django.shortcuts import render
from django.contrib import messages
from main.forms import QueryForm, NumberForm
from main.models import Query


def index(request):
    context = {
        "title": "Главная",
    }
    return render(request, "main/index.html", context)


def ping(request):
    title = "ping"
    if request:
        text = "Server is UP !"
    else:
        text = "Server is DOWN !"
    return render(request, "main/ping.html", {"title": title, "text": text})


def query(request):
    title = "Запрос"

    query_item = QueryForm(request.POST)
    if request.method == "GET":
        return render(
            request,
            "main/query.html",
            {"form": query_item, "title": title},
        )
    elif request.method == "POST":

        if query_item.is_valid():
            cadastral_number = query_item.cleaned_data["cadastral_number"]
            latitude = query_item.cleaned_data["latitude"]
            longitude = query_item.cleaned_data["longitude"]

            # эмуляция ожидания от сервера и его ответа на запрос
            time.sleep(random.randint(1, 60))
            result = random.choice([True, False])

            query = Query(
                cadastral_number=cadastral_number,
                latitude=latitude,
                longitude=longitude,
                result=result,
            )
            query.save()

            messages.success(
                request,
                f"Запрос успешно выполнен и сохранен, результат: {query.result}",
            )
            return render(
                request, "main/query.html", {"form": query_item, "title": title}
            )
        else:
            messages.error(
                request, f"Не получилось выполнить запрос, введены некорректные данные"
            )
            return render(
                request,
                "main/query.html",
                {"form": query_item, "title": title},
            )
    return render(
        request,
        "main/query.html",
        {"form": query_item, "title": title},
    )


def history(request):
    context = {
        "title": "history",
    }
    return render(request, "main/history.html", context)


def result(request):
    title = f"Все запросы"
    query_items = Query.objects.all()
    return render(
        request,
        "main/result.html",
        {"title": title, "query_items": query_items},
    )


def history_of_number(request):
    title = "Запрос по кадастровому номеру"

    query_item = NumberForm(request.POST)
    if request.method == "GET":
        return render(
            request,
            "main/query.html",
            {"form": query_item, "title": title},
        )
    elif request.method == "POST":

        if query_item.is_valid():
            cadastral_number = query_item.cleaned_data["cadastral_number"]
            query_items = Query.objects.filter(cadastral_number=cadastral_number)

            return render(
                request,
                "main/result.html",
                {"title": title, "query_items": query_items},
            )
        else:
            messages.error(
                request, f"Не получилось выполнить запрос, введены некорректные данные"
            )
            return render(
                request,
                "main/query.html",
                {"form": query_item, "title": title},
            )
    return render(
        request,
        "main/query.html",
        {"form": query_item, "title": title},
    )
