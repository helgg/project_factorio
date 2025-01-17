
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
# from django.views.generic import ListView, DetailView


def home(request):
    now = datetime.datetime.now()
    context = {}
    context['complete_date'] = now.strftime("%c")
    return render(request, 'home.html', context)

def blogs(request):

    posts = Blog.objects.all().order_by('-create_at')  
    context = {}
    context['posts'] = posts
    # context['forms'] = BlogForm()
    return render(request, 'blogs.html', context)

def make_a_post(request):
    context = {}
    context['forms'] = BlogForm()
    return render(request, 'post_article.html', context)

# class BlogsList(ListView):
#     model = Blog
#     template_name = 'blogs.html'
#     context_object_name = 'posts'

def blog_article(request, pk):

    post = get_object_or_404(Blog, pk=pk)  

    post.views += 1
    post.save(update_fields=['views'])

    # post = get_object_or_404(Blog, pk=pk)  
    context = {}
    context['post'] = post
    return render(request, 'blog_post.html', context)


# class BlogPostView(DetailView):
#     model = Blog
#     template_name = 'blog_post.html'
#     context_object_name = 'post'

def blog_register(request):
    form = BlogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.autor = request.user
            form.save()            
    return redirect('app:blogs')








