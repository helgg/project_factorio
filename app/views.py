
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, BlogView, Profile
from .forms import BlogForm

# renderiza a home
def home(request):
    now = datetime.datetime.now()
    context = {}
    context['complete_date'] = now.strftime("%c")
    return render(request, 'home.html', context)

# renderiza o catalogo de blogs (postagens)
def blogs(request):

    posts = Blog.objects.all().order_by('-create_at')  
    context = {}
    context['posts'] = posts
    return render(request, 'blogs.html', context)

# renderiza o form de postagem
def make_a_post(request):
    context = {}
    context['forms'] = BlogForm()
    return render(request, 'post_article.html', context)

# renderiza o artigo blog
def blog_article(request, pk):

    if request.user.is_authenticated:
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
    blog.save()
    context = {}
    context['post'] = blog
    return render(request, 'blog_post.html', context)


def blog_register(request):
    form = BlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('anonymous'):
                form.autor = None
            else:
                form.autor = request.user
            form.save()            
    return redirect('app:blogs')


def profile(request):
    user = Profile.objects.get(user=request.user)
    blogs = Blog.objects.filter(autor=request.user.id)
    context = {}
    context['blog_edit'] = blogs
    context['user'] = user
    # TODO: Caso nao logado redirecinar para login
    return render(request, 'profile.html', context)


def edit_blog(request,pk):

    blog = Blog.objects.get(autor=request.user.id, id=pk)
    form = BlogForm(data=request.POST or None, 
                    files=request.FILES or None,
                    instance=blog)
    
    if request.method == 'POST':  
        if form.is_valid():
            form.save()  
            return redirect('app:article', pk=blog.id)
        
    context = {}
    context['forms'] = form
    context['blog'] = blog
  
    return render(request, 'edit_blog.html', context)




def signin(request):
    
    return render(request, 'signin.html')











