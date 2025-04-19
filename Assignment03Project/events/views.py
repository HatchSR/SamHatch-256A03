from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm


# Create your views here.
def events(request):
    if request.method == "GET":
        # Check if the user is authenticated
        if request.user.is_authenticated:    

            # Check if the user is an not admin
            if request.session.get('role') != 'Admin':
                return render(request, 'events.html', {'events': Event.objects.all()})
            
            
            
            
            
            else: 
                
                return render(request, 'adminEvents.html', {'form': EventForm()})
        else:
            print('user is not authenticated')
            return redirect('loginaccount')
        
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        event = Event.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        event.save()
        return redirect('events')