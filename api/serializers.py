from rest_framework import serializers
from articles.models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("author", "title", "description",)

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("author", "title", "description", "article_text")
