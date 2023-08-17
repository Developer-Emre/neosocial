from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    post = Post.objects.all()
    category = Category.objects.all()
    
    context= {
        'post':post,
        'category':category
    }
    return render(request,'index.html',context)

def category(request, id):
    post = Post.objects.filter(category=id)
    category = Category.objects.all()
    
    
    context = {
        'category':category,
        'post':post
    }
    return render (request,'category.html',context)

def detail(request, postTitle):
    post= Post.objects.get(postTitle=postTitle)
    category = Category.objects.all()
    comment = Comment.objects.filter(commentPost=post)
    

    if request.method =='POST':
        comment =request.POST['comment']
        comn = Comment(commentText=comment,commentPost=post)
        comn.save()
        
        return redirect('/detay/' + post.postTitle + '/')

    context={
        'post':post,
        'comment':comment,
        'category':category
    }
    return render (request,'detail.html',context)