from django import forms
from .models import my_resume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.
class myform(forms.ModelForm):
    class Meta:
        model=my_resume
        fields=('__all__')


class register_form(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
        }








class myform(forms.ModelForm):
    
    class Meta:
        
        model = my_resume
        fields = ('__all__')

    
