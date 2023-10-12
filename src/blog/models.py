from django.db import models
from django.db.models import JSONField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    )

    CATEGORY_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snack', 'Snack'),
        ('Dinner', 'Dinner'),
    )

    title = models.CharField(max_length=200)
    body = models.TextField()
    duration = models.IntegerField(default=0)
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    ingredients = JSONField(default=list, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    banner = models.ImageField(
        upload_to='banners/', null=True, blank=True, default='default-recipe.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey('landing.CustomUser', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.title}"


class Conversation(models.Model):
    participant1 = models.ForeignKey(
        'landing.CustomUser', on_delete=models.CASCADE, related_name='conversations_as_participant1')
    participant2 = models.ForeignKey(
        'landing.CustomUser', on_delete=models.CASCADE, related_name='conversations_as_participant2')
    messages = models.ManyToManyField(
        'Message', blank=True)


class Message(models.Model):
    sender = models.ForeignKey('landing.CustomUser', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)