from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from women.models import Women, Category, TagPost

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
    posts = Women.published.all()
    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }
    return render(request, 'women/index.html', context=context)


def detail(request, slug):
    post = get_object_or_404(Women, slug=slug)
    print(post.category_id)
    data = {
        "title": post.title,
        "menu:": menu,
        "post": post,
        "cat_selected": post.category_id

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


def category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(category_id=cat.pk)
    context = {
        "title": f"Рубрика: {cat.title}",
        "menu": menu,
        "posts": posts,
        "cat_selected": cat.pk,
    }
    return render(request, 'women/index.html', context=context)


def show_tag_post_list(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'women/index.html', context=data)
