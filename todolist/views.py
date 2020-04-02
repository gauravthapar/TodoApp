from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, SignUpForm
from .models import Todo
from django.utils import timezone 
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todolist/home.html')


def signupuser(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('currenttodos')
        else:
            context = {
                'form': form,
                'error': form.errors
            }
            return render(request, 'todolist/signupuser.html', context )
    else:
        return render(request, 'todolist/signupuser.html', {'form': form})


def loginuser(request):
    if request.method == 'GET':
        context = {
            'form':AuthenticationForm()
        }
        return render(request, 'todolist/loginuser.html', context )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'username and password doest not match'
            }
            return render(request, 'todolist/loginuser.html', context )
        else:
            login(request,user)
            return redirect('currenttodos')


@login_required
def createtodo(request):
    if request.method == "GET":
        context = {
            'form': TodoForm()
        }
        return render(request, 'todolist/createtodo.html', context)
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit = False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            context = {
                'form': TodoForm(),
                'error': 'Bad data passed in. Try Again!'
            }
            return render(request, 'todolist/createtodo.html', context)


@login_required
def currenttodods(request):
    todos = Todo.objects.filter(user = request.user, datecompleted__isnull = True ).order_by('duedate')
    context = {
        'todos': todos
    }
    return render(request, 'todolist/currenttodos.html', context)


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user = request.user, datecompleted__isnull = False ).order_by('-datecompleted')
    context = {
        'todos': todos
    }
    return render(request, 'todolist/completedtodos.html', context)


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user = request.user)
    if request.method == "GET":
        form = TodoForm(instance = todo)
        context = {
            'todo': todo,
            'form': form
        }
        return render(request, 'todolist/viewtodo.html', context)
    else:
        try:
            form = TodoForm(request.POST, instance = todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            context = {
                'todo': todo,
                'form': form,
                'error': 'Bad data passed in. Try Again!'
            }
            return render(request, 'todolist/viewtodo.html', context)
            

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect("currenttodos")


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("currenttodos")


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

