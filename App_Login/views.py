from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from App_Login.forms import signUpForm, userProfileChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up(request):
    form = signUpForm()
    registered = False
    if request.method == "POST":
        form = signUpForm(data=request.POST)
        if form.is_valid(): 
            form.save()
            registered = True
    
    context = {"form": form, "registered": registered}
    return render(request, "App_Login/signup.html", context=context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("App_Login:profile"))

    context = {
        "form": form
    }
    return render(request, "App_Login/login.html", context=context)


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def profile_page(request):
    return render(request, "App_Login/profile.html")


@login_required
def profile_change(request):
    current_user = request.user
    form = userProfileChangeForm(instance = current_user)
    if request.method == "POST":
        form = userProfileChangeForm(request.POST, instance = current_user)
        if form.is_valid():
            form.save()
            form = userProfileChangeForm(instance = current_user)
    context = {
        "form": form
    }
    return render(request, "App_Login/change_profile.html", context=context)

@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user, data = request.POST)
        if form.is_valid():
            form.save()
            changed = True
    context = {
        "form": form,
        "changed": changed
    }
    return render(request, "App_Login/change_password.html", context=context)
