__author__ = 'glow'

from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.urlresolvers import reverse
from django.db import models
from sharpspark_ui.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from models import Contact

class ContactForm(forms.Form):
    name = forms.CharField("Your Name")
    email = forms.EmailField("Preferred Contact Email")
    contact_number = PhoneNumberField("Contact Phone Number")
    area_of_interest = forms.ChoiceField("Area of Interest",
                                         widget=forms.RadioSelect,
                                         )
    primary_mode = forms.ChoiceField("Preferred mode of Contact",
                                     widget=forms.RadioSelect,
                                     )
    comments = forms.CharField("Comments", widget=forms.Textarea)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field("name"),
        Field("email"),
        Field("contact_number"),
        Field("area_of_interest"),
        Field("primary_mode"),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
            )
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_number', 'primary_mode')

