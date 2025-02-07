from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    unique_views = models.PositiveIntegerField(default=0)
    anonymous_views = models.PositiveIntegerField(default=0)
    is_anonymous = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)  

    def __str__(self):
        author_name = self.author.get_full_name() if self.author else "Anônimo"
        return f"{self.title} - {author_name}"

    class Meta:
        db_table = "Blog"
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-create_at']


    
class BlogView(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="viewed_by")
  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return str(self.user) + ' - ' + str(self.blog)

    class Meta:
        unique_together = ('user', 'blog')
        db_table = "BlogView"
        verbose_name = "BlogView"
        verbose_name_plural = "BlogViews"


    







