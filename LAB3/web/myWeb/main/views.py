from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from .forms import PostForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
import logging
from . import async_methods
import asyncio
logger = logging.getLogger('django')


def main_page(request):
    return render(request, 'main/main_page.html', {'posts': asyncio.run(async_methods.get_all_posts())})


def faq(request):
    return render(request, 'main/faq.html')


def ad_detail(request, pk):
    return render(request, 'main/ad_detail.html', {'post': asyncio.run(async_methods.get_post_pk(pk))})


def add_new(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                logger.info(request.user.username + " add new ad ")
                return redirect('home')
            logger.error(request.user.username + " can't add new ad")
        else:
            form = PostForm()
        return render(request, 'main/ad_edit.html', {'form': form})
    return redirect('home')


def ad_edit(request, pk):
    post = asyncio.run(async_methods.get_post_pk(pk))
    if post.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                logger.info(request.user.username + " changed ad ")
                return redirect('ad_detail', pk=post.pk)
            logger.error(request.user.username + " can't change ad")
        else:
            form = PostForm(instance=post)
        return render(request, 'main/ad_edit.html', {'form': form})
    return redirect('home')


def ad_delete(request, pk):
    post = asyncio.run(async_methods.get_post_pk(pk))
    if post.author == request.user:
        post.delete()
        logger.info(request.user.username + " deleted ad ")
    return redirect('home')


def us_profile(request, pk):
    return render(request, 'main/profile.html', {'posts': asyncio.run(async_methods.get_filter_posts_by_author(pk))})


def do_logout(request):
    logger.info(request.user.username + " logout")
    logout(request)
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            logger.info(user_form.cleaned_data["username"] + " is new user")
            new_user.save()
            return redirect('signin')
        logger.error(user_form.cleaned_data["username"] + " failed sign up")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/signup.html', {'user_form': user_form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                logger.info(username + " sign in")
                login(request, user)
                return redirect("home")
            logger.error(username + " failed sign in")
    form = AuthenticationForm()
    return render(request=request, template_name="main/SignIn.html", context={"login_form": form})