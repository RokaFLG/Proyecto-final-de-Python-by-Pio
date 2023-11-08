from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, CompleteRegisterForm
from .models import CustomUser

# Create your views here.


def landing(request):
    return render(request, "landing/landing.html")


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("blog:home")
        else:
            request.session["valid_email"] = form.cleaned_data.get("email")
    else:
        valid_email = request.session.get("valid_email") or ""
        form = UserLoginForm(initial={"email": valid_email})

    context = {"form": form}
    return render(request, "landing/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")

            user = CustomUser.objects.create_user(
                email=email, username=username, password=password1
            )
            login(request, user)
            return redirect("complete-register")
        else:
            request.session["valid_email"] = form.cleaned_data.get("email")
            request.session["valid_username"] = form.cleaned_data.get(
                "username")
    else:
        valid_email = request.session.get("valid_email") or ""
        valid_username = request.session.get("valid_username") or ""

        form = UserRegisterForm(
            initial={"email": valid_email, "username": valid_username})

    context = {"form": form}

    return render(request, "landing/register.html", context)


@login_required(login_url='login')
def complete_register(request):
    user = request.user
    form = CompleteRegisterForm(instance=user)
    if request.method == "POST":
        form = CompleteRegisterForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("blog:home")

    return render(request, "landing/complete_register.html", {"form": form})


def about(request):
    return render(request, "landing/about.html")


def logout(request):
    django_logout(request)
    return redirect("login")