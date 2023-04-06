from django.urls import path
from .views import ArticleAPIView, ArticleDetailAPIView

urlpatterns = [
    path("", ArticleAPIView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail")
]
