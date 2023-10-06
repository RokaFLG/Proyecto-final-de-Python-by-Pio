
from django.shortcuts import render, get_object_or_404
from .models import Blog, Page

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

def about_me(request):
    return render(request, 'about_me.html')


from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Vista de registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog_list')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'page_detail.html', {'page': page})


from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm  

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect('blog_list')  
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm  

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.user == blog.author:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('blog_list')  
        else:
            form = BlogForm(instance=blog)
        return render(request, 'update_blog.html', {'form': form, 'blog': blog})
    else:
        
        return redirect('blog_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.user == blog.author:
        blog.delete()
        return redirect('blog_list')  
    else:
      
        return redirect('blog_list')

# blogapp/views.py

from django.contrib.auth.decorators import login_required, user_passes_test

# Define una función para verificar si el usuario es un administrador
def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Vista para crear un nuevo blog (protegida para administradores)
@login_required
@user_passes_test(is_admin)
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Recuperar datos del formulario
        if form.is_valid():
            # El formulario es válido, crear una instancia de Blog
            new_blog = form.save(commit=False)
            new_blog.author = request.user  # Asignar el autor del blog (puedes personalizar esto)
            new_blog.save()  # Guardar el blog en la base de datos
            return redirect('blog_list')  # Redirigir al usuario a la lista de blogs

    else:
        form = BlogForm()  # Si la solicitud no es POST, mostrar el formulario vacío

    return render(request, 'create_blog.html', {'form': form})
    

# Vista para editar un blog existente (protegida para administradores)
@login_required
@user_passes_test(is_admin)
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # Obtener el blog existente o mostrar un error 404 si no existe

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)  # Recuperar datos del formulario y usar la instancia existente
        if form.is_valid():
            # El formulario es válido, guardar los cambios en el blog
            updated_blog = form.save(commit=False)
            updated_blog.author = request.user  # Actualizar el autor si es necesario
            updated_blog.save()
            return redirect('blog_list')  # Redirigir al usuario a la lista de blogs después de la edición

    else:
        form = BlogForm(instance=blog)  # Si la solicitud no es POST, mostrar el formulario con los datos actuales del blog

    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

# Vista para eliminar un blog (protegida para administradores)
@login_required
@user_passes_test(is_admin)
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # Obtener el blog existente o mostrar un error 404 si no existe

    if request.method == 'POST':
        # Si la solicitud es POST, eliminar el blog
        blog.delete()
        return redirect('blog_list')  # Redirigir al usuario a la lista de blogs después de la eliminación

    return render(request, 'delete_blog.html', {'blog': blog})

from django.shortcuts import render

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

from django.shortcuts import render
from .models import Page

def page_list(request):
    pages = Page.objects.all()
    if not pages:
        message = "No hay páginas aún."
    else:
        message = None
    return render(request, 'page_list.html', {'pages': pages, 'message': message})

