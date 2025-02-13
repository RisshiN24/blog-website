from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    """
    Handles user signup by displaying a user creation form and processing
    form submissions. If the request method is POST and the form is valid,
    a new user is created and logged in, then redirected to the home page.
    Otherwise, it renders the signup form.
    """

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Check to see if the form is valid
            user = form.save()
            login(request, user)
            return redirect('home') # Sends the user to the home page
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def home(request):
    return render(request, 'blog/home.html')
