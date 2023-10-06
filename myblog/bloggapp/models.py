# blogapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/')

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

