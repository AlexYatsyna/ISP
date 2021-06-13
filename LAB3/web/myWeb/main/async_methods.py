from asgiref.sync import sync_to_async
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404


@sync_to_async
def get_all_posts():
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


@sync_to_async
def get_post_pk(pk):
    return get_object_or_404(Post, pk=pk)


@sync_to_async()
def get_filter_posts_by_author(pk):
    return Post.objects.filter(author=pk)