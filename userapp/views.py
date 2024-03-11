from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from .models import Blog



# Create your views here.


def index(request):
    return render(request,"index.html")



def post(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST['email']
        message=request.POST.get('message','')
        image=request.FILES.get('iname')
        date_time=request.POST.get('date_time')
        Blog.objects.create(
            name=name,
            email=email,
            message=message,
            image=image,
            date_time=date_time
        )
        
        
    return render(request,"post.html")



def blogview(request):
    return render(request,"blog.html")

#def blog_view(request,id):
    #blog = Blog.objects.get(id=id)
        #blog.likes += 1
        #blog.save()
    #blogdetails = Blog.objects.all()
    #context = {
        #'blogdetails':blogdetails
    #}
    #return render(request,"blog.html",context)

def blog_view(request, id):
    blog = get_object_or_404(Blog,id=id)
    user = request.user

    
    if user in blog.likes.all():
        
        blog.likes.remove(user)
    else:
        
        blog.likes.add(user)

    
    blog.save()

    
    blogdetails = Blog.objects.all()
    context = {
        'blogdetails': blogdetails
    }

    return render(request, "blog.html", context)
def check(request):
    blogdetails=Blog.objects.all()
    context={
        'blogdetails':blogdetails
    }
    return render(request,"check.html",context)

def edit(request,id):
    editdetails=Blog.objects.filter(id=id)
    context={
        'editdetails':editdetails
    }
    return render(request,"edit.html",context)

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        try:
            image=request.FILES['iname']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=Blog.objects.get(id=id).image
        Blog.objects.filter(id=id).update(
            name=name,
            email=email,
            message=message,
            image=file
        )
        return redirect("blogdetail")
    return render (request,"edit.html")



def delete(request,id):
    Blog.objects.filter(id=id).delete()
    return redirect("blogdetail")



def userregister(request):
    if request.method == "POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        Userdetails.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password
        )
        
    return render(request,"userregister.html")

def userblog(request):
    return render(request,"userblog.html")
def about(request):
    return render(request,"about.html")


def seeblog(request,bid):
    n=Blog.objects.filter(id=bid)
    context={
        'n':n
    }
    return render(request,"seeblog.html",context)

def user_profile(request, user_id):
    user = get_object_or_404(Userdetails, id=user_id)
    user_blogs = Blog.objects.filter(user=user.user)

    context = {
        'user': user,
        'user_blogs': user_blogs,
    }

    return render(request, 'user_profile.html', context)