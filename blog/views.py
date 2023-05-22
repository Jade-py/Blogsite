from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Post


def aboutView(request):
    return render(request, 'about.html')


def contactView(request):
    return render(request, 'contact.html')


class blog_post(DetailView):
    model = Post
    template_name = 'blog.html'


class homeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blogs_list'


class newBlogView(CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = ['title', 'author', 'body']


class updateBlogView(UpdateView):
    model = Post
    template_name = 'update_blog.html'
    fields = ['title', 'body']


class deleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

# Create your views here.
