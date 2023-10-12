from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.home, name='favorites'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('edit-recipe/<int:id>', views.edit_recipe, name='edit-recipe'),

    path('api/', include('blog.api.urls'))
]