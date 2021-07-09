from django.shortcuts import render,get_object_or_404, redirect
from .forms import CommentForm
from .models import Comment
from crudapp.models import Blog

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'form': form, 'post': post})

def commentupdate(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Blog, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'detail.html', {'update_form': form, 'post': post, 'comment': comment})

def commentdelete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Blog, pk=post_id)
    comment.delete()
    return redirect('detail', post_id=post.pk)