from django.contrib import admin
from .models import Blog, BlogView

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ...

@admin.register(BlogView)
class BlogAdmin(admin.ModelAdmin):
    ...
