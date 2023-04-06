from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from articles.models import Article, Source
from .serializers import ArticleListSerializer, ArticleDetailSerializer

class ArticleAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

class ArticleDetailAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
