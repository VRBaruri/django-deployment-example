
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcather=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcather(self):
        botcather = self.cleaned_data['botcather']
        if len(botcather)>0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcather
