from django.shortcuts import render,redirect
from django.contrib.auth.models import User
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

def register(request):
    
    if request.method =='POST':
        name = request.POST['firstname']
        surname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=name).exists():
                context = {
                    'information':'Bu kullanıcı sistemimizde mevcuttur. Farklı bir kullanıcı adı deneyiniz'
                }
                
                return render(request,'register.html',context)
            
            if User.objects.filter(email=email).exists():
                
                context = {
                    'information': 'Bu e-mail kullanılıyor. Farklı bir mail adresiyle kayıt olmayı deneyiniz.'
                }
                return render(request,'register.html',context)
            
            else:
                user = User.objects.create_user(username=name, email=email, first_name=name, last_name=surname,password=password)
                user.save()
                return redirect('kayıtol')
        else:
            context = {
                'information':'Parolanız tekrar parolanızla uyuşmuyor, tekrar kayıt olmayı deneyiniz.'
            }
            
            return render (request,'register.html',context)
    
    return render (request,'register.html')