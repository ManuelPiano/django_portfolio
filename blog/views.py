from django.shortcuts import render, get_object_or_404
from .models import post

def render_posts(request):
    posts = post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def post_detail(request, post_id):
    post_object = get_object_or_404(post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post_object})