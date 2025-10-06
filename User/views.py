from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from . import utils


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('user:profile')

    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        context = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        }

        if not (7 <= len(username) <= 30):
            messages.error(request, 'Username must be between 7 and 20 characters')
            return redirect('user:register')

        if not utils.check_password_case(password1):
            messages.error(request, 'Password must contain both uppercase and lowercase letters')
            return redirect('user:register')

        if not utils.check_password_case(password2):
            messages.error(request, 'Password must contain both uppercase and lowercase letters')
            return redirect('user:register')

        if not utils.check_password_numeric_and_symbols(password1):
            messages.error(request, 'Password must contain numeric and special characters')
            return redirect('user:register')

        if not utils.check_password_numeric_and_symbols(password2):
            messages.error(request, 'Password must contain numeric and special characters')
            return redirect('user:register')

        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, ', '.join(e.messages))
            return redirect('user:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists, choose another one')
            return redirect('user:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists, choose another one')
            return redirect('user:register')

        if password1 == password2:
            try:
                User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                         email=email, password=password1)
                messages.success(request, "Registration Successful. Please login to continue.")
                return redirect('user:login')
            except ValidationError as e:
                messages.error(request, ', '.join(e.messages))
                return redirect('user:register')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('user:register')
    else:
        return render(request, 'Register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('user:profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        context = {
            'username': username,
        }

        try:
            user_auth = auth.authenticate(request=request, username=username, password=password)

            if user_auth is not None:
                auth.login(request, user_auth)
                messages.success(request, 'You have successfully logged in.')
                return redirect('user:profile')
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'Login.html',context)

        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            render(request, 'Login.html',context)

    return render(request, 'Login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('user:login')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    return render(request, 'Profile.html')
