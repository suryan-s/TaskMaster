from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def login_(request):
    """
    This function renders the login page for the register app.
    :return:
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})


def register(request):
    """
    This function renders the register page for the register app.
    :return:
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # print("User created")
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register/signup.html', {'form': form})


def logout_(request):
    """
    This function logs the user out of the register app.
    :param request:
    :return:
    """
    logout(request)
    return redirect('/account/login/')
