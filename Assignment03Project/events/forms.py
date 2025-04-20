from django import forms

class EventForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 mb-4',
            'placeholder': 'Event Title'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 mb-4',
            'placeholder': 'Event Description',
            'rows': '4'
        })
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 mb-4'
        })
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 mb-4'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add labels with styling
        for field_name, field in self.fields.items():
            field.label = field.label or field_name.replace('_', ' ').capitalize()
            field.label_attrs = {'class': 'block text-sm font-medium text-gray-700 mb-1'}