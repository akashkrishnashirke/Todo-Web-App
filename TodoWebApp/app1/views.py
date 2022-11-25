from django.shortcuts import render,redirect
from .models import TodoMdel
from .forms import TodoForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse

@login_required()
def HomePage(request):
    return render(request,'home.html')

@login_required()
def all_tasks_view(request):
    all_task = TodoMdel.objects.all()
    return render(request,'all_task.html',{'all_task':all_task})

def signuot(request):
    logout(request)
    return redirect('/')

def add_task(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/all_tasks/')
    return render(request,'add_task.html',{'form':form})

def SignUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        return HttpResponse("data not valid....")
    return render(request,'SignUp.html',{'form':form})

def DeleteData(request,id):
    print("delete method call....")
    task = TodoMdel.objects.get(id__exact = id)
    print("task id",task)
    task.delete()
    return redirect('/all_tasks/')

def UpdateData(request,id):
    form = TodoMdel.objects.get(id = id)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=form)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        return HttpResponse("data not valide...")
    return render(request,'UpdateData.html',{'form':form})

@login_required()
def CompleteStatus(request):
    task = TodoMdel.objects.filter(status = 'complete')
    print(task)
    return render(request, 'CompleteStatus.html', {'form': task,})

@login_required()
def PendingStatus(request):
    task = TodoMdel.objects.filter(status = 'pending')
    print(task)
    return render(request, 'PendingStatus.html', {'form': task,})

def SearchTask(request):
    name = request.GET['name']
    form = TodoMdel.objects.filter(title__istartswith = name)
    return render(request,'Search.html',{'form':form})


