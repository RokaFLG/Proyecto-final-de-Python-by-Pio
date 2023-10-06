"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from django.urls import path
from . import views

urlpatterns = [
    
    path('blogs/', views.blog_list, name='blog_list'),

    
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]


from django.urls import path
from . import views

urlpatterns = [
   

    
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
]


from django.urls import path
from . import views

urlpatterns = [
    

    # Ruta para crear un nuevo blog (protegida para administradores)
    path('blogs/create/', views.create_blog, name='create_blog'),

    # Ruta para editar un blog existente (protegida para administradores)
    path('blogs/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),

    # Ruta para eliminar un blog (protegida para administradores)
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
