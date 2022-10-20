from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group(request, slug):
    return HttpResponse(f'Список групп {slug}')
