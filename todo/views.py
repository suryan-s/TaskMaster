from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TodoItemForm
from .models import TodoItem


@login_required(login_url='/account/login/')
def home(request):
    """
    This function renders the index page for the register app.
    :param request:
    :return:
    """
    # print(timezone.now())
    ongoing = TodoItem.objects. \
        filter(username=str(request.user.username)). \
        filter(deadline_at__gt=timezone.now()). \
        filter(is_completed=False). \
        order_by('deadline_at')
    expired = TodoItem.objects. \
        filter(username=str(request.user.username)). \
        filter(deadline_at__lt=timezone.now()). \
        filter(is_completed=False). \
        order_by('deadline_at')
    completed = TodoItem.objects. \
        filter(username=str(request.user.username)). \
        filter(is_completed=True). \
        order_by('deadline_at')

    content = {
        'ongoing': ongoing,
        'expired': expired,
        'completed': completed,
        'forms': TodoItemForm()
    }
    return render(request, 'home.html', content)


@login_required(login_url='/account/login/')
def add_todo(request):
    """
    This function adds a todo item to the database.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_new = TodoItem(
                username=str(request.user.username),
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                deadline_at=form.cleaned_data['deadline_at'],
                is_completed=False
            )
            todo_new.save()
            # print("New task added: ", todo_new.title)
            return redirect('/')
        else:
            print("Form is not valid")
            return redirect('/')


@login_required(login_url='/account/login/')
def complete_todo(request, todo_id: str):
    """
    This function marks a todo item as complete in the database.
    :param request: The request object.
    :param todo_id: The id of the todo item to mark as complete.
    :return:
    """
    todo_item = TodoItem.objects.\
        filter(username=str(request.user.username)).\
        filter(deadline_at__gt=timezone.now()).\
        get(title=todo_id)
    print(todo_item)
    todo_item.is_completed = True
    todo_item.save()
    return redirect('/')


@login_required(login_url='/account/login/')
def delete(request, todo_id: str):
    """
    This function deletes a todo item from the database.
    :param request:
    :return:
    """
    todo_item = TodoItem.objects. \
        filter(username=str(request.user.username)). \
        filter(deadline_at__gt=timezone.now()). \
        get(title=todo_id)
    todo_item.delete()
    return redirect('/')
