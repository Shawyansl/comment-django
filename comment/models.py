from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='comments')
    text = models.TextField( max_length=500 , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}..."