from django.shortcuts import render
from .models import Article, Source

#TODO: CBV

def article_list(request):
    """List all articles"""
    latest_article_list = Article.objects.order_by('-date_added')
    return render(request, 'articles/index.html', {'latest_article_list': latest_article_list})
    
def article_detail(request, aslug):
    """List all articles"""
    article = Article.objects.get(article_slug=aslug)

    return render(request, "articles/detail.html", {'article': article})
