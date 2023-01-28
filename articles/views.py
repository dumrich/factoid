from django.shortcuts import render
from .models import Article
from users.models import UserProfile
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django_filters.views import FilterView
from .filters import ArticleFilter


class ArticleSearchView(FilterView):
    filterset_class = ArticleFilter
    template_name = 'articles/search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


def show_category(request, category):
    """Show articles of only certain category"""
    page_number = request.GET.get("page")

    articles = Article.objects.filter(
        Q(category=category)).order_by('-id')

    paginator = Paginator(articles, 12)
    page_articles = paginator.get_page(page_number)

    return render(request, 'articles/category.html',
                  {'articles': page_articles,
                   'category': category})


@login_required
def article_list(request):
    """List all articles"""
    user_profile = UserProfile.objects.get(user=request.user)

    categories = user_profile.categories.all()
    categories_articles = []

    for category in categories:
        categories_articles.append(
            Article.objects.filter(category=category.name).order_by('-id')[:4])

    latest_article = Article.objects.latest('id')
    main_articles = Article.objects.filter(id__in=[34, 35, 36, 37])[1:4]

    # Politics

    return render(request, 'articles/index.html',
                  {'latest_article': latest_article,
                   'main_articles': main_articles,
                   'profile_arts': zip(categories, categories_articles),
                   'profile': user_profile})


def article_detail(request, aslug):
    """List all articles"""
    article = Article.objects.get(article_slug=aslug)

    return render(request, "articles/post_details.html", {'article': article})
