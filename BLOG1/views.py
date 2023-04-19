from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
# Create your views here.
def index(request):
    myposts = blogpost.objects.all()

    return render(request,'blog/blog.html',{'posts':myposts})




def Blogpost(request,blogid):
    
    post = blogpost.objects.filter(blog_id=blogid)[0]
    
    return render(request,'blog/blogpost.html',{'post':post})