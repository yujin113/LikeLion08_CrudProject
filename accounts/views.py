from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['username'] == "" or request.POST['password1'] == "" or request.POST['password2'] == "":
            return render(request, 'signup.html', {'error': '입력해주세요.'})
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 존재하는 Username 입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1']
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username이나 password가 일치하지 않습니다.'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')