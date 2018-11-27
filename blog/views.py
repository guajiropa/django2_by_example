"""
AUTHOR      :   Robert James Patterson
DATE        :   11/26/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Example' by Packt Publishing
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import EmailPostForm
from .models import Post

class PostListView(ListView):
    
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3 # Posts per page
    template_name = 'blog/post/list.html'  

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, 
                            publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    # get post by id
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields have passed validatiion
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
