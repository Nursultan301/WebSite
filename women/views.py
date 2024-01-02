from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {"title": "Главная страница", "url_name": 'home'},
    {"title": "О сайте", "url_name": 'about'},
    {"title": "Добавление статью", "url_name": 'add_page'},
    {"title": "Обратная связь", "url_name": 'contact'},
    {"title": "Войти", "url_name": 'login'},
]

db_data = [
    {"id": 1, "title": "Новость1", "is_published": True},
    {"id": 2, "title": "Новость2", "is_published": True},
    {"id": 3, "title": "Новость3", "is_published": False},
    {"id": 4, "title": "Новость4", "is_published": True}
]


def index(request):
    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": db_data
    }
    return render(request, 'women/index.html', context=context)


def detail(request, pk):
    return HttpResponse(f'Отображение статьи с id = {pk}')


def about(request):
    context = {
        "title": "О нас",
        "menu": menu
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')
