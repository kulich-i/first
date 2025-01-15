from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.views.generic import CreateView
from .models import Article

class ArticlesCreateView(CreateView):
    model = Article
    fields = ['article_title', 'article_text']  # поля для создания статьи 
    template_name = 'articles/create.html'  # шаблон для создания статьи   

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Не найдено")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Не найдено")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], pub_date = datetime.now() )

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

