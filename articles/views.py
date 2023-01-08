from django.shortcuts import render
from .models import Article


def article_list(request):
    """List all articles"""
    latest_article = Article.objects.latest('id')
    main_articles = Article.objects.order_by("-date_added")[1:4]

    return render(request, 'articles/index.html',
                  {'latest_article': latest_article,
                   'main_articles': main_articles})


def article_detail(request, aslug):
    """List all articles"""
    article = Article.objects.get(article_slug=aslug)

    return render(request, "articles/post_details.html", {'article': article})
