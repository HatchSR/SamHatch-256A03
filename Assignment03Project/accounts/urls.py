from django.urls import path
from . import views as accountViews

urlpatterns = [
    path('', accountViews.home,name='home'),
    path('signupaccount/', accountViews.signupaccount, name='signupaccount'),
    path('loginaccount/', accountViews.loginaccount, name='loginaccount'),
    path('logoutaccount/', accountViews.logoutaccount, name='logoutaccount'),
]