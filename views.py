from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView
from  django.views.generic.base import View
from .models import *


class AuthorsPage(ListView):
    model = Author
    context_object_name = "Authors"
    template_name = 'news/authors.html'

class PostDetail(View):
    def get(self, request, pk):
        ps = Post.objects.get(id=pk)
        return render(request, "news/posts.html", {'ps':ps})

def news_page_list(request):

    newslist = Post.objects.all().order_by('-rating')[:6]

    return render(request, 'news/news.html', {'newslist': newslist})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')