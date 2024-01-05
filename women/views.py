from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from women.models import Women

menu = [
    {"title": "Главная страница", "url_name": 'home'},
    {"title": "О сайте", "url_name": 'about'},
    {"title": "Добавление статью", "url_name": 'add_page'},
    {"title": "Обратная связь", "url_name": 'contact'},
    {"title": "Войти", "url_name": 'login'},
]

cats_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Певицы"},
    {"id": 3, "name": "Спортсменки"},
]


def index(request):
    posts = Women.objects.filter(is_published=True)
    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
    }
    return render(request, 'women/index.html', context=context)


def detail(request, slug):
    post = get_object_or_404(Women, slug=slug)
    data = {
        "title": post.title,
        "menu:": menu,
        "post": post,
        "cat_selected": 1

    }
    return render(request, 'women/detail.html', data)


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


def category(request, pk):
    context = {
        "title": "Отображение по рубрикам",
        "menu": menu,
        "posts": data_db,
        "cat_selected": pk,
    }
    return render(request, 'women/index.html', context=context)