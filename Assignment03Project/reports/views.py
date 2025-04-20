from django.shortcuts import redirect, render
from accounts.models import Person
from events.models import Event
from django.http import HttpResponse

# Create your views here.
def eventreports(request, event_id):

        
    if request.user.is_authenticated:
        if request.session.get('role') == 'Admin':
            registrants = []
            event = Event.objects.get(id=event_id)
            print(event.name, event.description, event.start_date, event.end_date, event.registered_users.all())
            for person in event.registered_users.all():
                registrants.append(person.user.username)
                
            print(event_id)
            eventInfo = {'name': event.name, 'description': event.description, 'start_date': event.start_date, 'end_date': event.end_date, 'registered_users': registrants}
            return render(request, 'reports.html', {'eventInfo': eventInfo})
        else:
            return redirect('events')

def userreports(request):
    if request.user.is_authenticated:
        if request.session.get('role') == 'Admin':
            person = []
            people={}
            for each in Person.objects.all():   
                person.append(each)
            print(person)
            for each in person:
                group_name = each.user_group.name if each.user_group else 'No Group'
                people.update({each.user.username: group_name})
                
            return render(request, 'userReports.html', {'person': people})
        else:
            return redirect('events')

    else:
        print('user is not authenticated')
        return redirect('loginaccount')
        
        
def registerReports(request):
    events = []
    if request.user.is_authenticated:
        for each in Event.objects.all():
            if Person.objects.get(user=request.user) in each.registered_users.all():
                events.append(each)
        print(events)
        return render(request, 'registerReports.html', {'events': events})
    else:
        print('user is not authenticated')
        return redirect('loginaccount')