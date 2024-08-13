from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Articles, Categories
from django.shortcuts import get_object_or_404
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
    model = Articles
    template_name = 'category.html'
    context_object_name = 'articles'  # Articles will be referred as 'articles' in the template
    paginate_by = 6

    def get_context_data(self, **kwargs):
        data = super(CategoriesDetail, self).get_context_data(**kwargs)
        data['title'] = "Time's Person"
        data['categories'] = Categories.objects.all().order_by('-date')
        data['categories_navbar'] = Categories.objects.filter(navbar=True).order_by('-date')

        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Categories, id=category_id)
        data['category_name'] = category.name
        return data

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(Categories, id=category_id)
            queryset = Articles.objects.filter(category=category).order_by('-date')
        else:
            queryset = Articles.objects.all().order_by('-date')
        return queryset