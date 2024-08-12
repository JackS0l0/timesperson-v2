from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Articles, Categories
class ArticleDetail(DetailView):
    model = Articles
    template_name = 'post.html'
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        data=super(ArticleDetail, self).get_context_data(**kwargs)
        data['title']=Articles.objects.get(pk=self.kwargs['pk'])
        data['categories']=Categories.objects.all().order_by('-date')
        data['categories_navbar']=Categories.objects.filter(navbar=True).order_by('-date')
        return data
class CategoriesDetail(ListView):
    model = Categories
    template_name = 'category.html'
    context_object_name = 'categories'
    def get_context_data(self, **kwargs):
        data=super(CategoriesDetail, self).get_context_data(**kwargs)
        data['title']="Time's Person"
        data['articles']=Articles.objects.all().order_by('-date')
        data['categories']=Categories.objects.all().order_by('-date')
        data['categories_navbar']=Categories.objects.filter(navbar=True).order_by('-date')
        return data