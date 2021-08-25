from django import forms
from django.forms import ModelForm

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    # email = forms.EmailField(
    #     max_length=50, help_text='characters not exceeding 255 chars')

    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        labels = {'name': 'Name'}

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
