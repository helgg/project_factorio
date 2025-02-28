from django.contrib import admin
from .models import Blog, BlogView

# Register your models here.

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    ...

@admin.register(BlogView)
class BlogView(admin.ModelAdmin):
    ...
