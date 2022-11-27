from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.


def RegisterUser(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is alredy taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is alredy taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are logged in now')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

    

@login_required(login_url='login')
def LogOut(request):
    logout(request)
    messages.success(request,'You are logged out')
    return redirect('login')


@login_required(login_url='login')
def Dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'user_contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)
