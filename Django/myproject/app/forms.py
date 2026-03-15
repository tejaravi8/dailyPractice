from django import forms
from .models import Skills

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ['name', 'level','experience']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
        }