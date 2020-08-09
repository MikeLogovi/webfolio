from django import forms
from .models import Website,Category

class WebsiteCreationForm(forms.ModelForm):
    category= forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Website
        fields=['title','category','description','image']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'custom-file-input'})
        }