from turtle import pos
from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all()
    # print(f"posts ==> {posts}")
    data = {
        "posts":posts
    }
    return render(request,'blog/home.html',context=data)


def details(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    print(post)
    context = {
        "post":post
    }
    return render(request,'blog/details.html',context)