import pytest
from main.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import get_object_or_404


@pytest.fixture
def user():
    return User.objects.create_user(username="Alisa", password="goodday")


@pytest.fixture
def post(user):
    return Post.objects.create(author=user, title="May", text="good luck", published_date=timezone.now())


@pytest.mark.django_db
def test_create_post(post):
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_author(post, user):
    assert post.author == user


@pytest.mark.django_db
def test_method_str(post):
    assert post.title == str(post)


@pytest.mark.django_db
def test_method_publish(post):
    post.publish()
    assert post == get_object_or_404(Post, pk=post.pk)