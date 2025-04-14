from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

class AuthenticateForm(AuthenticationForm):
    def __init__(self, request = ..., *args, **kwargs):
        super(AuthenticateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs.update({'class': "px-3 py-2 border border-gray-400 rounded-md w-full"})
            

class UserCreateForm(UserCreationForm):
    name = forms.CharField(label = 'Name')
    email = forms.EmailField(label = 'email')
    user_type = forms.ChoiceField(label = 'user type', choices=[('Reader','Reader'), ('Publisher','Publisher')], widget=forms.RadioSelect)
    def __init__(self, request = ..., *args, **kwargs, ):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['name','username','password1', 'password2','email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': "px-3 py-2 border border-gray-400 rounded-md w-full"})