from django import forms
from showcase_site.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control border-0', 'placeholder': 'Nom', 'style': 'height: 55px'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border-0', 'placeholder': 'Email', 'style': 'height: 55px'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control border-0', 'placeholder': 'Sujet', 'style': 'height: 55px'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control border-0', 'placeholder': 'Message', 'style': 'height: 55px'}),
        }
