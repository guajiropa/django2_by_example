"""
AUTHOR      :   Robert James Patterson
DATE        :   11/24/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Example' by Packt Publishing
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 Posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer than deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out-of-range than deliver the last page
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, 
                            publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


