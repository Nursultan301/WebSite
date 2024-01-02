from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная страница",
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {"title": "О нас"}
    return render(request, 'women/about.html', context=context)
