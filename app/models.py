from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # retorna o nome bonitinho do objeto no admin
        return self.title + ' - ' + str(self.autor)

    class Meta:
        db_table = "Blog"
    







