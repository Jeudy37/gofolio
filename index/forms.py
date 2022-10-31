from django import forms
from django import forms


from .models import Projet ,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('nom','siyati','email','telefon','foto')
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'siyati':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefon':forms.TextInput(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'})

        }




class ProjetForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields=('categori','titre','description','foto')

        widgets={
            'categori':forms.SelectMultiple(attrs={'class':'form-control'}),
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'})
        }