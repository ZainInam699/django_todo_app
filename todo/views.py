from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.
def home(request):
    # Add item
    if request.method == "POST":
        fm = ToDoForm(request.POST)
        if fm.is_valid():
            items = fm.cleaned_data['item']
            todo = ToDo(item = items)
            todo.save()
            fm = ToDoForm()
    else:
        fm = ToDoForm()
    content = ToDo.objects.all() 
    return render(request, 'todo/index.html', {'fm' : fm, "items":content})


def update(request, id):
    # Update item
    if request.method == 'POST':
        pk = ToDo.objects.get(pk=id)
        fm = ToDoForm(request.POST, instance = pk)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Item updated successfully!", fail_silently=True)
            return redirect('/')
    else:
        pk = ToDo.objects.get(pk=id)
        fm = ToDoForm(instance=pk)
    content = ToDo.objects.all() 
    return render(request, 'todo/index.html', {'fm':fm, "items":content, "status":"update"})

def delete(request, id):
    #delete item
    obj = ToDo.objects.get(pk=id)
    obj.delete()
    messages.error(request, "Item deleted successfully!", fail_silently=True)
    return redirect('/')

def clearAll(request):
    # clear all items
    all_items = ToDo.objects.all()
    for item in all_items:
        obj = ToDo.objects.get(pk=item.id)
        obj.delete()
    return redirect('/')