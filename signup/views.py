from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています。'})
        else:
            return render(request, 'signup.html')
