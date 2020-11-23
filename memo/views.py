from django.shortcuts import render
from memo.models import Memo
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

def home(request):
    memoList=Memo.objects.order_by('-idx')
    memoCount=Memo.objects.all().count()
    return render(request, 'memo/list.html',
        {'memoList':memoList, 'memoCount':memoCount})

@csrf_exempt
def insert_memo(request):
    memo=Memo(writer=request.POST['writer'],memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

def detail_memo(request):
    id=request.GET['idx']
    row=Memo.objects.get(idx=id)
    return render(request, 'memo/detail.html', {'row': row})

@csrf_exempt
def update_memo(request):
    id=request.POST['idx']
    memo=Memo(idx=id, writer=request.POST['writer'],
              memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

@csrf_exempt
def delete_memo(request):
    id=request.POST['idx']
    Memo.objects.get(idx=id).delete()
    return redirect('/memo')