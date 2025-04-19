from django.urls import path
from . import views as reportViews

urlpatterns = [
    path('reports/<int:event_id>', reportViews.eventreports,name='eventreports'),
    path('userreports/', reportViews.userreports,name='userreports'),
    path('registeredevents/', reportViews.registerReports,name='registeredevents'),
]