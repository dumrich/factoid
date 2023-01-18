from django.urls import path

from . import views

urlpatterns = [
    path('category/<str:category>', views.show_category, name='category_url'),
    path('', views.article_list, name='article_list'),
    path('search/', views.ArticleSearchView.as_view(), name='article_search'),
    path('<slug:aslug>/', views.article_detail, name='article_detail'),
]
