__author__ = 'glow'

from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.urlresolvers import reverse
from django.db import models
from sharpspark_ui.models import Contact

class ContactForm(forms.ModelForm):
    contact_number = PhoneNumberField()
    class Meta:
        model = Contact
