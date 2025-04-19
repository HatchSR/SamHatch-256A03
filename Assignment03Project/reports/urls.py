from django.urls import path
from . import views as reportViews

urlpatterns = [
    path('reports/<int:event_id>', reportViews.reports,name='reports'),
]