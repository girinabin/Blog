from django.shortcuts import render,redirect
from users.forms import Registrationform
from django.contrib.auth.decorators import login_required #profile ko lagi
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Account is created for {username}!')
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth.login(request, user)
        return redirect('blog-home')
    else:
        form = Registrationform()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'registration/profile.html')
