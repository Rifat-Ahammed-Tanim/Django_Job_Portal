from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users_auth_app.models import *

# register page view
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')

        if user_type == 'Admin':
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=phone,
                user_type=user_type,
                phone=phone
            )
            return redirect('login')
        else:
            PendingAccount.objects.create(
                username=username,
                email=email,
                phone=phone,
                user_type=user_type,
                painted_status='Pending'
            )
            return redirect('login')
    return render(request, 'auth/register.html')



# login page view
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'auth/login.html')

# dashboard page view
def dashboardPage(request):
    return render(request, 'auth/dashboard.html')