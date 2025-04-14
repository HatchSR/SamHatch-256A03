from django.shortcuts import render
from .models import Person
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import AuthenticateForm, UserCreateForm
from django.contrib import auth
from django.contrib.sessions.backends.db import SessionStore




def home(request):
    return render(request, 'home.html')
    #return render(request,'home.html')

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',{'form': UserCreateForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(request.POST.get('user_type'))
                user = Person.objects.create_user(request.POST['username'],name=request.POST['name'], email=request.POST['email'],user_type=request.POST.get('user_type'), password=request.POST['password1'])
                user.save()
                username = request.POST['username']
                print(f'USERNAME:{username}')
                

                login(request, user)
                request.session[username]
                print(f'SESSION NAME: {request.session.get('username')}')
                peron_info = Person.objects.all().filter(username = username)
                person_role = peron_info.values('user_type')
                request.session['role'] = person_role
                request.session.modified = True

                
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm(), 'error': 'User already exists'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm(), 'error': 'Passwords do not match'})


def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',{'form': AuthenticateForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        username = request.POST['username']
        print(f'USERNAME:{username}')
            
        request.session['username'] = username
        peron_info = Person.objects.all().filter(username = username)
        person_role = peron_info.values('user_type')
        # print(person_role)
        request.session['role'] = person_role[0]['user_type']
        
    
        
        # request.session['role'] = Person.user_type
        print(f'SESSION NAME: {request.session.get('username')}{request.session.get('role')}')
        request.session.modified = True
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticateForm(), 'error': 'Invalid username or password'})
        else:
            login(request, user)

            return redirect('home')