from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    unique_views = models.PositiveIntegerField(default=0)
    anonymous_views = models.PositiveIntegerField(default=0)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)  

    def __str__(self):
        return self.title + ' - ' + str(self.autor)

    class Meta:
        db_table = "Blog"

    
class BlogView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="viewed_by")  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return str(self.user) + ' - ' + str(self.blog)

    class Meta:
        unique_together = ('user', 'blog')
        db_table = "BlogView"


class Profile(models.Model):
    # TODO: Como garantir que ao criar um usuario, um profile seja criado?
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio_details = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True) 

    @property
    def blog_count(self):
        return Blog.objects.filter(autor=self.user).count()
    
    def __str__(self):
         return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = "Profile"


    







