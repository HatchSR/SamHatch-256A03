from django.shortcuts import render, redirect
from .models import Person, Group
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import AuthenticateForm, UserCreateForm
from django.contrib.auth.models import User
from django.http import HttpResponse
import re



def password_validation(password):
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")
     
    p = re.compile(regex)
 
    # If the string is empty 
    # return false
    if (password == None):
        return
 
    if(re.search(p, password)):
        return True
    else:
        return False
 


def home(request):
    return HttpResponse('<h1>Home</h1>')
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            if len(request.POST['password1']) > 6 and password_validation(request.POST['password1']):
                
                    try:
                        # Create Django User
                        user = User.objects.create_user(
                            username=request.POST['username'],
                            email=request.POST['email'],
                            password=request.POST['password1']
                        )
                        user.save()

                        # Find the Group object (your custom Group model)
                        print(f"Submitted user_type: {request.POST.get('user_type')}")
                        group_name = request.POST.get('user_type')  # From the form input
                        try:
                            group, created = Group.objects.get_or_create(name=group_name)
                            if created:
                                print(f"Created new group: {group_name}")
                            else:
                                print(f"Found existing group: {group_name}")
                            
                        except Group.DoesNotExist:
                            group = None  # Optional: handle this more gracefully

                        # Create the Person object
                        Person.objects.create(
                            user=user,
                            user_group=group
                        )

                        login(request, user)

                        request.session['username'] = user.username
                        request.session['role'] = group.name if group else 'No group'
                        request.session.modified = True

                        return redirect('events')

                    except IntegrityError:
                        return render(request, 'signupaccount.html', {
                            'form': UserCreateForm(),
                            'error': 'User already exists'
                        })
            else:
                return render(request, 'signupaccount.html', {
                    'form': UserCreateForm(),
                    'error': 'Password must be at least 6 characters, contain a uppercase, lowercase, special character and a number'
                })
        else:
            return render(request, 'signupaccount.html', {
                'form': UserCreateForm(),
                'error': 'Passwords do not match'
            })



def logoutaccount(request):
    logout(request)
    return redirect('loginaccount')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticateForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'loginaccount.html', {
                'form': AuthenticateForm(),
                'error': 'Invalid username or password'
            })
        else:
            login(request, user)

            try:
                person = Person.objects.get(user=user)
                request.session['username'] = user.username
                request.session['role'] = person.user_group.name if person.user_group else 'No group'
                request.session.modified = True
            except Person.DoesNotExist:
                request.session['username'] = user.username
                request.session['role'] = 'No person profile'

            return redirect('events')
