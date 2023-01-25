from django.http import HttpResponse
from django.shortcuts import render

from board.models import BoardModel


def boardfunc(request):
    return HttpResponse('bord')


def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})
