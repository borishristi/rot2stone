from django import forms
from showcase_site.models import Devis


class ContactForm(forms.ModelForm):
    SERVICE_CHOICES = (
        ('Service1', 'Notre service 1'),
        ('Service2', 'Notre service 2'),
        ('Service3', 'Notre service 3'),
        ('Service4', 'Notre service 4'),
    )

    service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Devis
        fields = ('name', 'email', 'date', 'service', 'message',)
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control border-0', 'placeholder': 'Nom', 'style': 'height: 55px'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border-0', 'placeholder': 'Email', 'style': 'height: 55px'}),
            'date': forms.DateTimeInput(
                attrs={'class': 'form-control border-0 datetimepicker-input', 'placeholder': 'Date de rappel',
                       'style': 'height: 55px', 'data-target': '#date', 'data-toggle': 'datetimepicker'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control border-0', 'placeholder': 'Message', 'style': 'height: 55px'}),
        }
