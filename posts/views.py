from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Gett all posts, limit = 20
    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html'),
    {'posts': posts}
