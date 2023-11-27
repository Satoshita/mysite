from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_date')[:]
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', ctx)

