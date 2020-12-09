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

def delete(request):
    return render(request, 'delete.html')