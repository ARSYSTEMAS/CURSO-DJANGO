from django import forms


class forms_contact(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje= forms.CharField()
