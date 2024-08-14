from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Articles, Categories,Contact,About,Partnors,AboutinFooter
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
        data['aboutinfooter']=AboutinFooter.objects.all()[0:1]
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
        data['aboutinfooter']=AboutinFooter.objects.all()[0:1]
        return data
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(Categories, id=category_id)
            queryset = Articles.objects.filter(category=category).order_by('-date')
        else:
            queryset = Articles.objects.all().order_by('-date')
        return queryset
def about(request):
    data={
        'title':"Time's Person - About",
        'about':About.objects.all()[0:1],
        'categories' : Categories.objects.all().order_by('-date'),
        'categories_navbar':Categories.objects.filter(navbar=True).order_by('-date'),
        'aboutinfooter':AboutinFooter.objects.all()[0:1],
    }
    return render(request,'about.html',data)
def contact(request):
    data={
        'title':"Time's Person - Contact",
        'contact':Contact.objects.all()[0:1],
        'categories' : Categories.objects.all().order_by('-date'),
        'categories_navbar':Categories.objects.filter(navbar=True).order_by('-date'),
        'aboutinfooter':AboutinFooter.objects.all()[0:1],
    }
    return render(request,'contact.html',data)
def partnors(request):
    data={
        'title':"Time's Person - Partners",
        'partnors':Partnors.objects.all().order_by('-date'),
        'categories' : Categories.objects.all().order_by('-date'),
        'categories_navbar':Categories.objects.filter(navbar=True).order_by('-date'),
        'aboutinfooter':AboutinFooter.objects.all()[0:1],
    }
    return render(request,'partnors.html',data)
def search(request):
    data={
        'title':"Time's Person - Search",
        'articles':Articles.objects.all().order_by('-date'),
        'categories' : Categories.objects.all().order_by('-date'),
        'categories_navbar':Categories.objects.filter(navbar=True).order_by('-date'),
        'aboutinfooter':AboutinFooter.objects.all()[0:1],
    }
    return render(request,'search.html',data)