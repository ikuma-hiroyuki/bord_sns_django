from django.contrib.auth import authenticate, login
from django.shortcuts import render


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'board.html')
        else:
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが間違っています。'})
    else:
        return render(request, 'login.html', {'context': 'ログインしてください。'})
