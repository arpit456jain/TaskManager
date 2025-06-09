from django.shortcuts import render,redirect
from home.models import Task 
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    if request.method == 'POST':
        taskname = request.POST['taskname']
        taskdesc = request.POST['taskdesc']
        entry = Task(taskTitle=taskname,taskDesc=taskdesc,user=request.user)
        entry.save()
        messages.success(request,'Task is added successfully!')
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def task(request):
    allTasks = Task.objects.filter(user=request.user)
    context = {"allTasks":allTasks}
    return render(request,'task.html',context)


@login_required(login_url='/accounts/login/')
def deletetask(request,id):
    if request.method=="GET":
        task = get_object_or_404(Task, id=id, user=request.user)
        try:
            task.delete()
            messages.success(request,'task is successfully deleted!')
            return redirect('task')
        except:
            messages.error(request,'Some error occured!!')
    
    return HttpResponse('del')
@login_required(login_url='/accounts/login/')
def edittask(request,id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        taskname = request.POST['taskname']
        taskdesc = request.POST['taskdesc']
        task.taskTitle = taskname
        task.taskDesc = taskdesc
        task.save()
        return redirect('task')
    context = {"title":task.taskTitle,"desc":task.taskDesc}
    return render(request,'edit.html',context)
