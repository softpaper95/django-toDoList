from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from makeList.models import Post #객체 Post의 내용(메소드)을 가져옴


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
