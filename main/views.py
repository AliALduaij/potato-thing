from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles_list.html", context)


def article_details(request, article_id):
    context = {"article": Article.objects.get(id=article_id)}
    return render(request, 'article_details.html', context)
