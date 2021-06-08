import asyncio
from django.shortcuts import render, redirect
from django.utils.decorators import classonlymethod
from django.views.generic import View
from django.urls import reverse
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from asgiref.sync import sync_to_async

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


@sync_to_async
def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts})

@sync_to_async
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class LoginView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @sync_to_async
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts_list_url')
        context = {}
        return render(request, 'blog/login.html', context)

    @sync_to_async
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts_list_url')
        else:
            messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'blog/login.html', context)

class LogoutView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @sync_to_async
    def get(self, request):
        logout(request)
        return redirect('posts_list_url')

    @sync_to_async
    def post(self, request):
        pass


class RegisterView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @sync_to_async
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts_list_url')

        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'blog/register.html', context)

    @sync_to_async
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect(reverse('login_url'))
        return render(request, 'blog/register.html', context={'form': form})


class ProfileView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    @sync_to_async
    def get(self, request):
        curr_user = request.user
        posts = Post.objects.filter(user=curr_user)

        return render(request, 'blog/user_profile.html', context={'posts': posts})

    @sync_to_async
    def post(self, request):
        pass