from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    url = forms.CharField(label='url', max_length=100)

    class Meta:
        model = Url
        fields = ('url',)
