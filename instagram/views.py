from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html instagram/templates 까지는 고정된 주소
    # render 로 html 파일로 보내줌
    return render(request, 'instagram/post_list.html', {
        'post_list1' : qs, # template 에서 사용할 이름 지정
        'q' : q
    }
                  )