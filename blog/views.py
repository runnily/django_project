from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    """
    Handles traffic from homepage of our blog
    """
    #this is what is going to be assessed in our html
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',  context)

def about(request):
    return render(request, 'blog/about.html', {"title": "About"}) 
