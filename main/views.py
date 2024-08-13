from django.shortcuts import render
from articles.models import Categories,Articles
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.db.models import Q
from django.utils import translation
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def index(request):
    data={
        'title': "Time's Person",
        'categories': Categories.objects.all().order_by('-date'),
        'categories_navbar': Categories.objects.filter(navbar=True).order_by('-date'),
        'articles': Articles.objects.all().order_by('-date'),
        'articles_slide': Articles.objects.filter(slide=True).order_by('-date')[0:3],
        'articles_slide2': Articles.objects.filter(slide2=True).order_by('-date')[0:3],
        'articles_slide3': Articles.objects.filter(slide3=True).order_by('-date')[0:2],
        'articles_1': Articles.objects.all().order_by('-date')[0:1],
        'articles_2': Articles.objects.all().order_by('-date')[1:2],
        'articles_3': Articles.objects.all().order_by('-date')[2:3],
        'articles_412': Articles.objects.filter(Q(category__name='Business') | Q(category__name='Бизнес') | Q(category__name='Biznes')).order_by('-date')[0:6],
        'articles_1318': Articles.objects.filter(Q(category__name='Events') | Q(category__name='События') | Q(category__name='Hadisələr')).order_by('-date')[0:6],
        'articles_face_last2': Articles.objects.filter(Q(category__name='Faces') | Q(category__name='Лица') | Q(category__name='Simalar')).order_by('-date')[0:2],
    }
    return render(request,'index.html',data)