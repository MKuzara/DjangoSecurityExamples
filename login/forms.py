from django import forms

from .models import ExampleUser

class LoginForm(forms.ModelForm):
    
    username = forms.CharField(max_length=25, min_length=6, error_messages={
        'invalid': 'Enter valid username'
    })

    class Meta:
        model = ExampleUser
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }