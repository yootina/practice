from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    # {% url 'articles:index %}
    # return redirect('articles:index')
    return redirect('articles:detail', id=article.id)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')

def edit(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article' : article,
    }
    return render(request, 'edit.html', context)

def update(request, id):
    # 새로운정보
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 기존정보
    article = Article.objects.get(id=id)
    # 갈아끼우기
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', id=article.id)