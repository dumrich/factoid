from django.urls import path

from . import views

urlpatterns = [
    path('sign-up', views.sign_up, name="sign_up")
]
