from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_mgr.forms import RegistrationForm, LoginForm, UserAccountForm
from user_mgr.models import UserAccount
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    #return HttpResponse('welcome to user_mgr')
    context = {
        
    }
    return render(request, 'user_mgr/index.html', context)

def create_account(request):
    reg_form = RegistrationForm()
    context = {
        'reg_form': reg_form
    }
    if request.method == 'POST':
        user = None
        user_reg_form = RegistrationForm(data = request.POST)
        rp = request.POST
        if User.objects.filter(email = rp['email']).exists():
            context['reg_form'] = user_reg_form
            messages.info(request, 'Sorry this email has been taken')
            return redirect(reverse('user_mgr:register'))
        else:
            if user_reg_form.is_valid():
                #user_reg_form.save()
                user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'], )
                user.set_password(rp['password'])
                user.save()
                #create a useraccount for the new customer
                useraccount = UserAccount.objects.create(user = user)
                #messages.success(request, 'Your details have been saved')
                if user:
                   messages.success(request, 'Your details have been saved')
                else:
                    messages.warning(request, 'something went wrong acount not created!! please try again!')
            else: 
                #since django uses uersername and we checked for email only is_valid is False when we enter
                #username a username that alraedy exists so to tackle that we use the else and do this.
                #messages.warning(request, 'Username already exists!!')
                context['reg_form'] = RegistrationForm(data = request.POST)
    return render(request, 'user_mgr/login.html', context)

def log_in(request):
    login_form = LoginForm()
    context = { 'login_form' : login_form }
    if request.method == 'POST':
        rp = request.POST
        login_form = LoginForm(data = request.POST)
        #check if user exists
        if User.objects.filter(email = rp['email']).exists():
            username = User.objects.get(email = rp['email']).username
            auth_user = authenticate(username= username, password = rp['password'])
            if auth_user:
                login(request, auth_user)
                return HttpResponse('<h1>You have been logged in!!<\h1>')
            else: 
                context['login_form'] = login_form
                messages.error(request, 'Sorry your email or password is incorrect!!')
        else: 
            context['login_form'] = login_form
            messages.error(request, 'Sorry this email adddress doest not exist!!')
            
    context['login_form'] = login_form
    return render(request, 'user_mgr/login.html', context)
