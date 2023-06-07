from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.access_count +=1
        self.object.save()
        return super().get(self, request, *args, **kwargs)

class homeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blogs_list'

    def get_queryset(self):
        return Post.objects.order_by("-access_count")


class newBlogView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class updateBlogView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_blog.html'
    fields = ['title', 'body']


class deleteBlogView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')


class userDashboardView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user_dashboard.html'


class userBlogView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'all_blogs_list'
    template_name = 'user_posts.html'



# Create your views here.
