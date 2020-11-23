from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    name='방문자'
    msg='안녕하세요.'
    return render(request, 'memo/index.html',
                  {'name':name, 'msg':msg})