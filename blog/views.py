"""
AUTHOR      :   Robert James Patterson
DATE        :   12/02/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Example' by Packt Publishing
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from .models import Post, Comment

class PostListView(ListView):
    
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3 # Posts per page
    template_name = 'blog/post/list.html'  

def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, 
                            publish__month=month, publish__day=day)
    # List all active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted 
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object, but do not write to db just yet.
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save to database
            new_comment.save()

    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post/detail.html', {'post': post, 
                                                        'comments': comments, 
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form})


def post_share(request, post_id):
    # get post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields have passed validatiion
            cd = form.cleaned_data
            # Get post URL
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # Build email
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], 
                                                                cd['email'], 
                                                                post.title)

            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, 
                                                                    post_url, 
                                                                    cd['name'], 
                                                                    cd['comments'])
            # Send email
            send_mail(subject, message, 'thepattersonthree@gmail.com', [cd['to']])
            sent = True
    else:
        # Return the form
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 
                                                    'form': form,
                                                    'sent': sent})
