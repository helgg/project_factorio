
import datetime

from django.shortcuts import render, redirect
from authentication.models import User
from .models import Blog, BlogView
from .forms import BlogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# renderiza a home
def home(request):
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'

    now = datetime.datetime.now()
    context = {}
    context['profile'] = user
    context['complete_date'] = now.strftime("%c")
    return render(request, 'home.html', context)

# renderiza o catalogo de blogs (postagens)
def blogs(request):
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'

    posts = Blog.objects.all().order_by('-create_at')  
    context = {}
    context['profile'] = user
    context['posts'] = posts
    return render(request, 'blogs.html', context)

# renderiza o form de postagem
def make_a_post(request):
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'
    context = {}
    context['profile'] = user
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
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'
    context = {}
    context['profile'] = user
    context['post'] = blog
    return render(request, 'blog_post.html', context)

@login_required
def blog_register(request):    
    form = BlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('anonymous'):
                form.is_anonymous = True
            else:
                form.is_anonymous = False
            form.author = request.user
            form.save()            
    return redirect('app:blogs')

@login_required(login_url="/login")
def profile(request):
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'
    blogs = Blog.objects.filter(author=request.user.id)
    context = {}
    context['blog'] = blogs
    context['profile'] = user
    # TODO: Caso nao logado renderizar para login
    
    return render(request, 'profile.html', context)


def edit_blog(request,pk):

    blog = Blog.objects.get(author=request.user.id, id=pk)
    form = BlogForm(data=request.POST or None, 
                    files=request.FILES or None,
                    instance=blog)
    
    if request.method == 'POST':  
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('anonymous'):
                form.is_anonymous = True
            else:
                form.is_anonymous = False
            form.save()  
            return redirect('app:article', pk=blog.id)
        
    try:
        user = User.objects.get(user=request.user.id)
    except Exception:
        user = 'sem usuario logado'
    context = {}
    context['profile'] = user
    context['forms'] = form
    context['blog'] = blog
  
    return render(request, 'edit_blog.html', context)


# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None: 
#                 # TODO: Tratativa de erros de login
#                 login(request, user)
#                 return redirect('/') 
#     else:
#         form = AuthenticationForm()

#     context = {}
#     context['form'] = form
    
#     return render(request, 'login.html', context)



# def signin(request):

#     return render(request, 'signin.html')









