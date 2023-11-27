from django.shortcuts import render
from .models import Post

def home(request):
    blogs = Post.objects.all().order_by('-created_date')[:]
    ctx = {
        'blogs': blogs,
    }
    return render(request, 'home.html', ctx)
