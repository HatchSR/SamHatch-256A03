from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm
from accounts.models import Person


# Create your views here.
def events(request):
    if request.method == "GET":
        # Check if the user is authenticated
        if request.user.is_authenticated:
            person = Person.objects.get(user=request.user)
            return render(request, 'events.html', {'events': Event.objects.all(),'person': person})
        else:
            print('user is not authenticated')
            return redirect('loginaccount')
    if 'register_event' in request.POST:
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        print(request.user)
        person = Person.objects.get(user=request.user)
    
        event.registered_users.add(person)
        return redirect('events')
    if 'unregister_event' in request.POST:
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        person = Person.objects.get(user=request.user)
        event.registered_users.remove(person)
        return redirect('events')
                
def adminEvents(request):
    if request.method == "GET":
        # Check if the user is authenticated
        if request.user.is_authenticated:
            if request.session.get('role') == 'Admin':
                return render(request, 'adminEvents.html', {'form': EventForm(), 'events': Event.objects.all()})
            else:
                return redirect('events')
        else:
            print('user is not authenticated')
            return redirect('loginaccount')
        
    if request.method == "POST":
        
        if 'create_event' in request.POST:
            title = request.POST.get("title")
            description = request.POST.get("description")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")

            event = Event.objects.create(
                name=title,
                description=description,
                start_date=start_date,
                end_date=end_date
            )
            event.save()
            return redirect('events')
                
        elif 'edit_event' in request.POST:
                    event_id = request.POST.get('event_id')
                    if event_id:
                        event = get_object_or_404(Event, id=event_id)

                        event.name = request.POST.get("title", event.name)
                        event.description = request.POST.get("description", event.description)
                        event.start_date = request.POST.get("start_date", event.start_date)
                        event.end_date = request.POST.get("end_date", event.end_date)
                        event.save()

                    return redirect('events')

                # DELETE EVENT
        elif 'delete_event' in request.POST:
                    event_id = request.POST.get('event_id')
                    if event_id:
                        event = get_object_or_404(Event, id=event_id)
                        event.delete()
                    return redirect('events')
        elif 'report' in request.POST:
            event_id = request.POST.get('event_id')
            if event_id:
                event = get_object_or_404(Event, id=event_id)
            
            return redirect('reports', event_id=event_id)

            # Fallback redirect
        return redirect('events')