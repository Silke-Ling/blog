from django.shortcuts import render

# Create your views here.

from .models import Article

def index(request):
    #取出所有文章
    articles=Article.objects.all()
    #需要传递给模板（templates）的对象
    context={'articles':articles }
    #render函数：载入模板，并返回context对象
    return render(request,'index.html',context)

import markdown

def article(request,id):
    #取出相应文章
    article=Article.objects.get(id=id)
    #markdown渲染
    article.body=markdown.markdown(article.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    context={'article':article}
    return render(request,'article/detail.html',context)
