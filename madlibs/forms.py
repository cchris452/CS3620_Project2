from django import forms
from .models import madlibs

class MadLibForm(forms.ModelForm):
    class Meta:
        model = madlibs
        fields = ['name', 'place', 'adjective', 'color', 'animal', 'feeling', 'verb']