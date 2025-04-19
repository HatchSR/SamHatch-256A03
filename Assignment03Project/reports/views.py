from django.shortcuts import render

# Create your views here.
def reports(request, event_id):
    print(event_id)
    return render(request, 'reports.html')