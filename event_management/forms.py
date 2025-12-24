from django import forms
from .models import Customer_Details, program_tbl, event, feedback_tbl
from datetime import date

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer_Details
        fields = ['name', 'email', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProgramForm(forms.ModelForm):
    class Meta:
        model = program_tbl
        fields = ['event_name', 'venue', 'date', 'district', 'description', 'image']

    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError("Date cannot be in the past.")
        return selected_date

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['name', 'place', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback_tbl
        fields = ['feedback']