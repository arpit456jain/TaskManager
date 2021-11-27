from django.shortcuts import render,redirect
from home.models import Task 
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        taskname = request.POST['taskname']
        taskdesc = request.POST['taskdesc']
        entry = Task(taskTitle=taskname,taskDesc=taskdesc,user=request.user)
        entry.save()
        print("true")
    return render(request,'index.html')

# Create your views here.
def task(request):
    print(request.user.id)
    if request.user.id == None:
        print("login needed")
    else:
        allTasks = Task.objects.filter(user=request.user)
        context = {"allTasks":allTasks}
        print(allTasks)
        return render(request,'task.html',context)
    return render(request,'task.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = user = User.objects.create_user(username, 'email', password)
        user.save()
    else:
        print("get")
        
    return render(request,"signup.html")

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            print("invalid")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

def deletetask(request,slug):
    if request.method=="GET":
        print("get")
        slug=int(slug)
        print(slug,type(slug))
        # x = Task.objects.filter(id=id).delete()
        x = Task.objects.get(id = slug)  
        print(x)
        try:
            x.delete()
            # messages.success(request,'task is successfully deleted!')
            return redirect('/task/')
        except:
            messages.error(request,'Some error occured!!')
    else:
        print('not get')
    return HttpResponse('del')

def edittask(request,slug):
    task = Task.objects.get(id = slug) 
    if request.method == "POST":
        print("post")
        taskname = request.POST['taskname']
        taskdesc = request.POST['taskdesc']
        # print(taskname,taskdesc)
        # entry = Task(taskTitle=taskname,taskDesc=taskdesc,user=request.user)
        # entry.save()
        print(task.taskTitle,task.taskDesc)
        task.taskTitle = taskname
        task.taskDesc = taskdesc
        task.save()
        print(task.taskTitle,task.taskDesc)
        return redirect('/task/') 
    context = {"title":task.taskTitle,"desc":task.taskDesc}
    print(context)
    return render(request,'edit.html',context)

def todo(request):
    return render(request,'todo.html')