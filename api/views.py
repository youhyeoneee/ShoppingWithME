from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 메인 화면
def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})

# 정보 입력 화면
def enter_info(request):
    msg = 'My Message'
    return render(request, 'enter_info.html', {'message': msg})

# 쇼핑 화면
def shop(request):
    msg = 'My Message'
    return render(request, 'shop.html', {'message': msg})