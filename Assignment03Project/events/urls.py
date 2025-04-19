from django.urls import path
from . import views as eventViews

urlpatterns = [
    path('', eventViews.events,name='events'),
    path('adminEvents/', eventViews.adminEvents,name='adminEvents'),

]