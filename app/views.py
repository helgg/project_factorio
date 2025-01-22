
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, BlogView
from .forms import BlogForm


def home(request):
    now = datetime.datetime.now()
    context = {}
    context['complete_date'] = now.strftime("%c")
    return render(request, 'home.html', context)

def blogs(request):

    posts = Blog.objects.all().order_by('-create_at')  
    context = {}
    context['posts'] = posts
    return render(request, 'blogs.html', context)

def make_a_post(request):
    context = {}
    context['forms'] = BlogForm()
    return render(request, 'post_article.html', context)


def blog_article(request, pk):

    if request.user.is_authenticarted:
        try:
            BlogView.objects.get(user=request.user, blog=pk)
            blog = Blog.objects.get(id=pk)
        
        except Exception:
            blog = Blog.objects.get(id=pk)
            BlogView.objects.create(user=request.user, blog=blog)
            blog.unique_views += 1
            blog.views = blog.unique_views + blog.anonymous_views
    else:
        blog = Blog.objects.get(id=pk)
        blog.anonymous_views += 1

    blog.views = blog.unique_views + blog.anonymous_views
    blog.save(update_fields=['views', 'unique_views', 'anonymous_views'])

    context = {}
    context['post'] = blog
    return render(request, 'blog_post.html', context)


def blog_register(request):
    form = BlogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.autor = request.user
            form.save()            
    return redirect('app:blogs')








