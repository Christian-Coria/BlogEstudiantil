from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontchat(request):
    return render(request, 'chat/frontchat.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontchat')
    else:
        form = SignUpForm()
    
    return render(request, 'chat/signup.html', {'form': form})