from django.shortcuts import render,redirect
from .models import TodoModel
from .forms import TodoForm
from django.contrib import  messages

# Create your views here.

def home(request):
    task = TodoModel.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Task added in a list")
        return redirect('/')

    context = {'task':task,'form':form}
    return render(request,'home.html',context)


def update(request,pk):
    tasks = TodoModel.objects.get(id=pk)
    form = TodoForm(instance=tasks)
    if request.method=='POST':
        form = TodoForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()

        return redirect('home')
    context = {'form':form}
    return render(request,'update.html',context)


def delete(request,pk):
    item = TodoModel.objects.get(id=pk)
    if request.method=='POST':
            item.delete()
            return redirect('home')
            #messages.success(request,'Task has deleted..')
    context = {'item':item}
    return render(request,'delete.html',context)

# Demo line

    