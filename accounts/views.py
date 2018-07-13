from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request, 'accounts/signup.html', {'error': f'Username {user.username} has already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST.get('username'), request.POST.get('password'))
                user.set_password(request.POST['password1'])
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords doesn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        print(request.POST)
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
