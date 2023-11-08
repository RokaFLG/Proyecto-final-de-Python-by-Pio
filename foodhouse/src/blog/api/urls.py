from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.favorites),
    path('add-favorites/', views.add_favorite),
    path('delete-favorites/', views.delete_favorite),
    path('liked-recipes/', views.liked_recipes),
    path('like/', views.like),
    path('unlike/', views.unlike),
    path('delete-recipe/', views.delete_recipe),
    path('create-conversation', views.create_conversation),
    path('create-message', views.create_message),
    path('messages', views.get_messages),
]