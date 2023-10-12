from django.contrib import admin
from .models import Recipe, Category, Message, Conversation

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Conversation)