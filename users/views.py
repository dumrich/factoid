from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CheckboxForm
from .models import Category, UserProfile
from django.urls import reverse

# Create your views here.


@login_required
def profile(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CheckboxForm(request.POST)
        if form.is_valid():
            for option in form.cleaned_data['options']:
                category = Category.objects.create(name=option)
                user_profile.categories.add(category)
        else:
            form = CheckboxForm()

    context = {'user_profile': user_profile, 'form': CheckboxForm}
    return render(request, 'users/profile.html', context)


def sign_up(request):
    """List all articles"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/sign_up.html", {"form": form})
