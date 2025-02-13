from django import forms
from .models import User

from django.contrib.auth.forms import AuthenticationForm


class EmployeeForm(forms.ModelForm):
    reporting_manager = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        required=False,  
        empty_label="Select Reporting Manager", 
        label="Reporting Manager"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'mobile', 
                  'dept', 'role', 'reporting_manager', 'date_of_joining']
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['reporting_manager'].queryset = User.objects.exclude(pk=self.instance.pk)
        else:
            self.fields['reporting_manager'].queryset = User.objects.all()

    
    def clean_reporting_manager(self):
        reporting_manager = self.cleaned_data.get('reporting_manager')
        if reporting_manager == self.instance:
            raise forms.ValidationError("An employee cannot be their own reporting manager.")
        return reporting_manager


     

class LoginForm(AuthenticationForm):
    pass
        