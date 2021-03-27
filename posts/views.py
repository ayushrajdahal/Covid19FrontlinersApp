from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import CommentForm
from .models import Post, Tweet
from marketing.forms import EmailSignupForm
from marketing.models import Signup
from .twitter import set_inactive, set_active, save_to_db


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def index(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    emailform = EmailSignupForm()
    email_function(request)

    context = {
        'latest': latest,
        'emailform': emailform
    }
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()


    post_list = Post.objects.order_by('-timestamp')

    paginator = Paginator(post_list, 3)

    page_request_var = 'page'

    page = request.GET.get(page_request_var)

    email_function(request)

    emailform = EmailSignupForm()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count': category_count,
        'emailform': emailform,
    }

    return render(request, 'blog.html', context)


# for the repetitive email code


def email_function(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


# /email_function()


def post(request, id):
    category_count = get_category_count()
    latest = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    emailform = EmailSignupForm()
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': post.id
            }))
    context = {
        'form': form,
        'post': post,
        'latest': latest,
        'category_count': category_count,
        'emailform': emailform,
    }
    return render(request, 'post.html', context)


def about(request):
    emailform = EmailSignupForm()
    context = {
        'emailform': emailform,
    }
    return render(request, 'about.html', context)



@login_required
def tweet_list(request):
    tweets = Tweet.objects.order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 10)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_set_inactive(request, pk):
    set_inactive(pk)
    return redirect('tweet_list')


@login_required
def tweet_set_active(request, pk):
    set_active(pk)
    return redirect('tweet_list')


@login_required
def tweet_fetch(request):
    save_to_db()
    return redirect('tweet_list')

def faq(request):
    emailform = EmailSignupForm()
    context = {
        'emailform': emailform,
    }
    return render(request, 'faq.html', context)