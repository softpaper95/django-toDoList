from django.shortcuts import render,redirect, get_object_or_404#있지도 않은 글(객체)를 요청하면 404에러를 띄우자!
from django.utils import timezone
from makeList.models import Post #객체 Post의 내용(메소드)을 가져옴
from .forms import PostForm ##


# Create your views here.
def home(request):
    return render(request, 'home.html')

def write(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    #장고는 필드이름(published_date)와 연산자 필터(lte)를 밑줄 2개를 사용해 구분합니다.
    return render(request, 'write.html', {"posts": posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})

def post_new(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)#()에 commit=False를 넣으면 넘겨진 데이터를 바로 Post모델에 저장시키지 말라는 뜻이다. 보통
        post.created_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk) #post_detail 페이지는 반복문으로 post들이 출력되므로 각 post마다의 pk값이 필요하다.

    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) #수정하고자 하는 글의 Post 모델을 instance로 가져옴(pk로 원하느 글을 찾는다.)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('write')
    