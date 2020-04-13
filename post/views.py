from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    if(Post.objects.count == 0):
        slider1 = Slider.objects.get(id=1)
        return render(request,'home.html')
    else:
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 2)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        slider1 = Slider.objects.get(id=1)
        slider2 = Slider.objects.get(id=2)
        slider3 = Slider.objects.get(id=3)
        slider4 = Slider.objects.get(id=4)
        """ilk x reklam anasayfa x-2x e kadar başka kategori"""
        """reklam1Anasayfa = Ad.objects.get(id=1)
        reklam2Anasayfa = Ad.objects.get(id=2)"""
        context ={
            'posts' : posts,
            'page_obj':page_obj,
            'slider1':slider1,
            'slider2': slider2,
            'slider3': slider3,
            'slider4': slider4,
        }
        return render(request,'home.html',context)

def Bursaspor(request):
    posts = Post.objects.filter(categorie = '1').order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request,'home.html',context)


def PostDetail(request,title):
    post = Post.objects.get(title = title)
    context = {
        'post':post,
    }
    return render(request,'detail.html',context)