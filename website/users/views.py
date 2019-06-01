from django.shortcuts import render,redirect
from users.forms import Registrationform
from django.contrib.auth import login,authenticate
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
        return redirect('blog-home')
    else:
        form = Registrationform()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'registration/profile.html')
