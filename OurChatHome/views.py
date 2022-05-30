from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def frontpage(request):
    return render(request, 'OurChatHome/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
        
    else:
        form = SignUpForm()

    return render(request, 'OurChatHome/signup.html', {'form': form})


