from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, ScheduledPost, SocialMediaAccount
from .forms import PostForm, CommentForm, ScheduledPostForm
from .social_api import fetch_mock_twitter_posts, fetch_mock_facebook_posts
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Like
from .forms import ScheduledPostForm
from .models import ScheduledPost
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LogoutView
from django.db.models import Count

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    user_accounts = SocialMediaAccount.objects.filter(user=request.user)

    # Fetch mocked posts from social APIs
    mock_social_posts = []
    for acc in user_accounts:
        if acc.platform == 'twitter':
            mock_social_posts += fetch_mock_twitter_posts(acc.account_name)
        elif acc.platform == 'facebook':
            mock_social_posts += fetch_mock_facebook_posts(acc.account_name)

    # Handle post submission
    if request.method == 'POST' and 'post_submit' in request.POST:
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')
    else:
        post_form = PostForm()

    # Handle comment submission
    if request.method == 'POST' and 'comment_submit' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = get_object_or_404(Post, id=post_id)
            new_comment.save()
            return redirect('home')
    else:
        comment_form = CommentForm()

    return render(request, 'dashboard/home.html', {
        'posts': posts,
        'mock_posts': mock_social_posts,
        'post_form': post_form,
        'comment_form': comment_form,
    })

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # If already liked, unlike
    return redirect('home')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('home')


@login_required
def schedule_post(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST)
        if form.is_valid():
            scheduled = form.save(commit=False)
            scheduled.user = request.user
            scheduled.save()
            return redirect('schedule_post')
    else:
        form = ScheduledPostForm()

    scheduled_posts = ScheduledPost.objects.filter(user=request.user).order_by('-scheduled_time')

    return render(request, 'dashboard/schedule_post.html', {
        'form': form,
        'scheduled_posts': scheduled_posts
    })

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')

class LogoutViewAllowGET(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def analytics(request):
    user = request.user
    total_posts = Post.objects.filter(user=user).count()
    total_likes = Like.objects.filter(post__user=user).count()
    total_comments = Comment.objects.filter(post__user=user).count()

    most_liked_post = (
        Post.objects.filter(user=user)
        .annotate(num_likes=Count('likes'))
        .order_by('-num_likes')
        .first()
    )

    most_commented_post = (
        Post.objects.filter(user=user)
        .annotate(num_comments=Count('comments'))
        .order_by('-num_comments')
        .first()
    )

    return render(request, 'dashboard/analytics.html', {
        'total_posts': total_posts,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'most_liked_post': most_liked_post,
        'most_commented_post': most_commented_post,
    })  

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')