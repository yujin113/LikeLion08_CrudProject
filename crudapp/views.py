from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Blog.objects
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Blog, pk = post_id)
    return render(request, 'detail.html', {'post': post_detail})

def postcreate(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})

def postupdate(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    post.delete()
    return redirect('home')