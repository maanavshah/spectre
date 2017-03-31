from models import Post, Hit, Comment
from forms import PostForm, RegisterForm, LoginForm, HitForm, CommentForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
import django.contrib.auth
from django.contrib.auth import logout as django_logout
from django.core.management import call_command


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login(request):
    form = LoginForm(request.POST or None)  # 'None' removes 'this field required' problem
    if '_submit' in request.POST:
        if form.is_valid():
            user = form.login()
            if user:
                django.contrib.auth.login(request, user)
                return HttpResponseRedirect("/spectre/")
            else:
                context = {'message': 'login_invalid'}
                return render(request, 'login.html', context)
    
    # Hit-Count For Login 
    try:
        hit=Hit.objects.get(tag='Login',ip_address=get_client_ip(request))
        hit.hit_count=int(hit.hit_count)+1
    except:
        hit=Hit.objects.create(tag='Login', hit_count=1, last_hit=timezone.now(), ip_address=get_client_ip(request))
    hit.hit_now()
    hit.ip_address = get_client_ip(request)
    hit.save()
    return render(request, 'login.html', {'form':form})

def register(request):
    form = RegisterForm(request.POST or None)
    if '_submit' in request.POST:
        if form.is_valid():
            try:
               User.objects.create_user(username=form.cleaned_data['username'],
                                     email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password'])
            except:
                context = {'user_message': 'user_conflict'}
                return render(request, 'register.html', context)
        else:
            context = {'email_message': 'register_invalid'}
            return render(request, 'register.html', context)

    # Hit-Count For Register 
    try:
        hit=Hit.objects.get(tag='Register',ip_address=get_client_ip(request))
        hit.hit_count=int(hit.hit_count)+1
    except:
        hit=Hit.objects.create(tag='Register', hit_count=1, last_hit=timezone.now(), ip_address=get_client_ip(request))
    hit.hit_now()
    hit.ip_address = get_client_ip(request)
    hit.save()
    return render(request, 'register.html', {'form': form})

def reviews(request):
    query = request.GET.get('query_name')
    print query
    if '_logout' in request.GET:
        logout(request)
        return HttpResponseRedirect("/spectre/")
    if request.user.is_authenticated():
        context = {'user_message': 'user_session'}
        posts = Post.objects.filter(author=request.user).order_by('-published_date')
    else:
        context = {'none_message': 'none_session'}
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'reviews.html', {'posts': posts, 'context': context})

def review(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated():
        context = {'user_message': 'user_session'}
        if request.user == post.author:
            context = {'user_message': 'user_session', 'control_message': 'user_valid'} 
    else:
        context = {'none_message': 'none_session'}
    if '_delete' in request.GET:
        Post.objects.filter(pk=pk).delete()
        return HttpResponseRedirect('/spectre/')
    if '_edit' in request.GET:
        return HttpResponseRedirect('/spectre/reviews/edit')
    return render(request, 'review.html', {'post': post, 'context': context})

def add_review(request):
    if request.user.is_authenticated():
        context = {'user_message': 'user_session'}
    else:
        context = {'none_message': 'none_session'}
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return HttpResponseRedirect('/spectre/')
    return render(request, 'reviews_post.html', {'form': form, 'context': context})

def reviews_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print post.title
    if request.user.is_authenticated():
        context = {'user_message': 'user_session'}
    else:
        context = {'none_message': 'none_session'}
    form = PostForm(request.POST or None)
    if form.is_valid():
        Post.objects.filter(pk=pk).delete()
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return HttpResponseRedirect('/spectre/')
    return render(request, 'reviews_edit.html', {'form': form, 'post':post, 'context': context})

def about(request):
    return render(request, 'about.html', {})

def logout(request):
    if request.user.is_authenticated():
        print request.user
        django_logout(request)
        return  HttpResponseRedirect('/spectre/')

def hits(request):
    posts = Hit.objects.filter()
    return render(request, 'hits.html', {'posts': posts})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/spectre/')
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return HttpResponseRedirect('/spectre/')

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return HttpResponseRedirect('/spectre/')