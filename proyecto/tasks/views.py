from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django. contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import tasks
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request,'home.html',{'form': UserCreationForm
    })

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html',{'form': UserCreationForm
    })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user =   User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render (request,'signup.html',{
                    'form': UserCreationForm,"error": 'el usuario ya existe'
                })
         
          #register user  
            
    return render(request,'signup.html',{'form': UserCreationForm, "error": 'contraseña incorrecta'
    })

def task(request):
    
    if request.method == 'GET':
        Task=tasks.objects.filter(User=request.user)     
        return render(request,'tasks.html', {
            'tasks':Task, 'form':TaskForm
        })

def create_task(request):

    if request.method =='GET':
        return render(request,'create_tasks.html',{
           'form':TaskForm
    })
    else:
        form=TaskForm(request.POST)
        N_tarea=form.save(commit=False)
        N_tarea.user= request.user
        N_tarea.save()
        print(N_tarea)
        return redirect('home')
    
        

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html', {'form':AuthenticationForm
 })
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html', {'form':AuthenticationForm,'error':'usuario o contraseña incorrectos'})
        
        else:
            login(request, user)
            return redirect('tasks')
        
       