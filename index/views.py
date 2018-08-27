import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
import markdown
from .models import *

def index_views(request):
    return HttpResponse('......')


def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})


def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
