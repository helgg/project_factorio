from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import Blog

class User(AbstractUser):
    bio_details = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True) 

    @property
    def blog_count(self):
        return Blog.objects.filter(author=self).count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
        
    class Meta:
        db_table = "user"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"