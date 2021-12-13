from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html', 
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)

    if request.method == 'POST':
        print("")
        form = PostForm(request.POST, request.FILES, instance=post)
    
        if form.is_valid():            
            form.save()        
            return HttpResponseRedirect('/')

        else:            
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm        
    return render(request, 'edit.html',
                  {'post': post, 'form': form})

def LikeView(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post.id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True 
    return HttpResponseRedirect(post.get_absolute_url())
