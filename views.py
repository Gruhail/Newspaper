from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import NewsForm
from django.urls import reverse_lazy
from .filters import PostFilter


class Posts(ListView):
    model = Post
    template_name = 'news/base.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = NewsForm
    template_name = 'news/post_create.html'
    #success_url = reverse_lazy('home')


class PostEdit(UpdateView):
    form_class = NewsForm
    model = Post
    # success_url = reverse_lazy('home')
    template_name = 'news/post_create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news/deletepost.html'
    success_url = reverse_lazy('home')
    context_object_name = 'deletenews'














