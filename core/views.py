from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from room.views import room 
from django.contrib import messages
# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')




# Create your views here.
# Home page
def index(request):
    return render(request, 'core/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('room')  # Redirect to the 'room' URL name
            else:
                # Add an error message indicating invalid credentials
                messages.error(request, 'Invalid username or password. Please try again.')
        # If form is not valid or authentication fails, re-render the login form
        # with the entered data and error messages.
        return render(request, 'core/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})
# logout page
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the 'login' URL name