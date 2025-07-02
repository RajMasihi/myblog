from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Post
# Create your views here.

def home(request):
    #load all data post
    posts=Post.objects.all().order_by('-post_id')
    cats=Category.objects.all().order_by('-cat_id')
    data={
        'cats':cats,
        'posts':posts
    }
    return render(request, 'home.html', data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all().order_by('-cat_id')
    return render(request, 'posts_page.html', {'post':post, 'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat).order_by('-post_id')
    return render(request, 'category_post.html', {'cat':cat, 'posts':posts})

