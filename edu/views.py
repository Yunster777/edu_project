from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import PostForm


def post_list(request):
    # PostList 조회
    posts = Post.objects.all()

    # 변수를 넘길 context 만들기
    context = {
        "posts": posts,
    }

    # 템플릿 파일에 데이터를 담은 사전인 context를 넘기면서 render
    return render(request, "edu/post_list.html", context)


def post_detail(request, post_id):
    # Post Detail 조회
    post = Post.objects.get(pk=post_id)

    # 변수를 넘길 context 만들기
    context = {
        "post": post,
    }

    # 템플릿 파일에 데이터를 담은 사전인 context를 넘기면서 render
    return render(request, "edu/post_detail.html", context)


# 로그인 안하면 common:login으로 보내는 데코레이터(장고 기본 제공)
@login_required(login_url="common:login")
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("edu:post_list")
    else:
        form = PostForm()

    context = {
        "form": form,
    }

    return render(request, "edu/post_form.html", context)


@login_required(login_url="common:login")
def post_edit(request, post_id):
    # post 불러오기
    post = get_object_or_404(Post, pk=post_id)

    # post 작성자가 현재 로그인한 유저가 맞는지
    if request.user != post.user:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect("edu:post_detail", post_id=post.id)

    # post 일 때는 수정 작업
    # get 일 때는 폼에 instance만 채워주기
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.updated_at = timezone.now()
            post.save()
            return redirect("edu:post_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "edu/post_form.html", context)


@login_required(login_url="common:login")
def post_delete(request, post_id):
    # post 불러오기
    post = get_object_or_404(Post, pk=post_id)

    # post 작성자가 현재 로그인한 유저가 맞는지
    if request.user != post.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("edu:post_detail", post_id=post_id)

    # post 일 때 삭제 작업
    post.delete()
    return redirect("edu:post_list")
