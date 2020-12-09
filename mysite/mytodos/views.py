from django.shortcuts import render
from mytodos.models import *
from mytodos.forms import *
# Create your views here.


def home(request):
    todo_list = todo.objects.all()
    add_todos = add_todo()

    if request.method == "POST":
        add_todos = add_todo(request.POST)

        if add_todos.is_valid():
            add_todos.save(commit=True)

        
    mydict = {'todos':todo_list, 'add_todos':add_todos}
    return render(request, 'index.html', context=mydict)



def update(request,todo_id):
    todo_list = todo.objects.get(pk = todo_id)
    update_todos = add_todo(instance= todo_list)
    

    if request.method == "POST":
        update_todos = add_todo(request.POST, instance = todo_list)

        if update_todos.is_valid():
            update_todos.save(commit=True)
            return render(request, 'success.html')
    mydict = {'update_todo': update_todos}
    return render(request, 'update.html', context = mydict)


def delete(request,todo_id):
    mytodo = todo.objects.get(pk=todo_id).delete()
    return render(request, 'delete.html')