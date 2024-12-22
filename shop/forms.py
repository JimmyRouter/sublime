from django import forms

from shop.models import Tickets


class FeedbackForm(forms.ModelForm):
    client_email = forms.EmailField(label='Your Email')
    client_phone = forms.IntegerField(label='Your Phone')
    client_name = forms.CharField(label='Your Name')
    ticket_subject = forms.CharField(label='Subject', widget=forms.Textarea(attrs={'class': 'form-input','rows':3, 'cols':60}))

    def client_info(self):
        return self.data

    class Meta:
        model = Tickets
        fields = ('client_email', 'client_phone', 'client_name', 'ticket_subject')
