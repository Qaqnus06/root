from .models  import User
from django  import forms

class RegisterForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','first_name' ,'last_name','email','password']
    def clean_username(self):
        username=self.cleaned_data['username']
        if len(username)<4 or len (username)>30:
            raise forms.ValidationError('username 4 va 30 oraligida bolish kerak')
        return username 
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data['username']
        if len(username)<4 or len (username)>30:
            raise forms.ValidationError('username 4 va 30 oraligida bolish kerak')
        return username
    
class ProfileUpdateForm(forms.BaseModelForm):

    class Meta:
        model=User
        fields=['username','first_name' ,'last_name','email','password']
            
        