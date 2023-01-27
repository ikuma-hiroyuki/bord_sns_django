from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from board.models import BoardModel


def boardfunc(request):
    return HttpResponse('bord')


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    post = get_object_or_404(BoardModel, pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read += 1
        object.readtext += username + '\n'
        object.save()
        return redirect('list')
