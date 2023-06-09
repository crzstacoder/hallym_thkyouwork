from django.shortcuts import render
from .models import Post

# Create your views here.

def thankyoupost_list(request) :
    posts = Post.objects.all()
    return render(request, 'thankyoupost_list.html', {'posts' : posts})