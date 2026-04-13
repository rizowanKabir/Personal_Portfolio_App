from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Job Opportunity / Collaboration'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell me about your project...', 'rows': 5}),
        }
