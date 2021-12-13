from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        username = request.POST['username']

        if password == confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Taken')
                return redirect('../register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This Username is Taken')
                return redirect('../register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
                user.save()
                return redirect('../login')
        else:
            print("Password not matching")
            return redirect('../register')
        return redirect('/')
    else:
        return render(request, 'register.html')