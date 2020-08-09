from  django.contrib.auth.forms  import UserCreationForm
from django import forms
from .models import Developper
from django.contrib.auth import authenticate
class DevelopperFormRegister(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Votre mot de passe'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Confirmer votre mot de passe'}),
    )
    class Meta:
        model = Developper
        fields = ['username','email','password1','password2','prefered_language','picture']
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':"Votre nom d'utilisateur",}),
            'email' :forms.EmailInput(attrs={'class':'form-control','placeholder':"Votre adresse email",'type':'email'}),
            'prefered_language': forms.Select(attrs={'class':'form-control'},choices=[('Python','Python'),('Java','Java'),('C/C++','C/C++'),('Php','Php')]),
            'picture' :forms.FileInput(attrs={'class':'form-control'})      
        }

class DevelopperFormLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Votre mot de passe'}))
    class Meta:
        model = Developper
        fields=['email','password']
        widgets={
            'email' :forms.EmailInput(attrs={'class':'form-control','placeholder':"Votre adresse email",'type':'email'}),
        }
        
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if  not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid credentials")

               