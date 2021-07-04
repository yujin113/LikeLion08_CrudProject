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

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})