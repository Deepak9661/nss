from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):

    return render ( request, 'home.html',{'name':"bharti"})
def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    
    return render (request, 'result.html',{'result':res})
def register(request):
        if request.method == 'POST':
        first_name = request.POST['first_name']
        Last_name = request.POST['Last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save():
        print('user_created')
        return redirect('/')
         else:
            return render(request,'register.html')
