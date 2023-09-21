from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.


def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todoApp/index.html', {'todo_items': todo_items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        task=request.POST['task']
        todo_item = TodoItem(title=title,task=task)
       # print(todo_item)
        todo_item.save()
        return redirect('todo_list')
    return render(request, 'todoApp/add_todo.html')

def search_todo(request):
    if request.method=='POST':
        title_query =request.POST['title']
        completed_query =request.POST['completed']
        todo_items = TodoItem.objects.all()
        if title_query:
            todo_items = todo_items.filter(title__icontains=title_query)
            if completed_query == 'true':
                todo_items = todo_items.filter(completed=True)
                print(todo_items)
            else:
                todo_items = todo_items.filter(completed=False)
                print(todo_items)

        search_results = {
            'todo_items': todo_items,
            'title_query': title_query,
            'completed_query': completed_query,
        }
        return render(request,'todoApp/search_result.html',search_results)
    return render(request,'todoApp/search_todo.html')
   
    
def search_result(request):
    return render(request,'todoApp/search_todo.html')

def view_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    return render(request, 'todoApp/view_todo.html', {'todo_item': todo_item})


def edit_todo(request,todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task=form.cleaned_data['task']
            completed = form.cleaned_data['completed']
            todo_item=TodoItem(title=title,task=task,completed=completed)
            todo_item.save()
            # Update the TODO item using title and completed
            # Save the changes to the database
            return redirect('view_todo', todo_id=todo_item.id)
    else:
        form = TodoItemForm(initial={'title': todo_item.title, 'task':todo_item.task,'completed': todo_item.completed})
    return render(request, 'todoApp/edit_todo.html', {'form': form, 'todo_item': todo_item})



def delete_todo(request,todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list')
    return render(request, 'todoApp/delete_confirm.html', {'todo_item': todo_item})
