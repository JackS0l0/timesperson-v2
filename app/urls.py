from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main import views as mainviews
from articles import views as articlesviews
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='homepage'),
    path('articles/<slug:slug>/<int:pk>/',articlesviews.ArticleDetail.as_view(),name='articledetail'),
    path('category/<slug:slug>/<int:category_id>/',articlesviews.CategoriesDetail.as_view(),name='categoriesDetail'),
    path('about/',articlesviews.about,name='aboutpage'),
    path('contact/',articlesviews.contact,name='contactpage'),
    path('partners/',articlesviews.partnors,name='partnorspage'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", mainviews.set_language, name="set-language"),
] 