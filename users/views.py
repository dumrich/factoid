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
            user_profile.categories.clear()
            for option in form.cleaned_data['options']:
                category = Category.objects.create(name=option)
                user_profile.categories.add(category)
        else:
            form = CheckboxForm()

    context = {'user_profile': user_profile, 'form': CheckboxForm}
    return render(request, 'users/profile.html', context)


def sign_up(request):
    """Sign Up view for user authentication"""
    if request.method == 'POST':
        # When they send the form...
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login user
            login(request, user)

            # Redirect to home page
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    # Return Registration page
    return render(request, "registration/sign_up.html", {"form": form})
