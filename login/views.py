from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def index(request) :
    return render(request, 'login/login.html')

def show_List(request) :
     if request.method == 'POST':
        # 폼 제출 처리 (필요시)
        return HttpResponseRedirect((reverse('main')))  # 'main'은 urls.py에서 정의한 URL 이름입니다.
        # 'showList.html'은 폼을 포함한 페이지입니다.

def main_view(request):
    return render(request, 'main.html')  # 'main.html' 페이지를 렌더링합니다.