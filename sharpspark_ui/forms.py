__author__ = 'glow'

from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.urlresolvers import reverse
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from models import ContactRequest, Course


class ContactForm(forms.Form):
    name = forms.CharField("Your Name")
    email = forms.EmailField("Preferred Contact Email")
    contact_number = PhoneNumberField(label="Contact Number")
    area_of_interest = forms.ChoiceField(label="Area of Interest",
                                         choices=ContactRequest.INTEREST_AREA)
    primary_mode = forms.ChoiceField(label="Preferred mode of Contact",
                                     choices=ContactRequest.CONTACT_MODES)
    comments = forms.CharField("Comments", widget=forms.Textarea)

    helper = FormHelper()
    helper.form_class = 'form-vertical'
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
        model = ContactRequest
        fields = ('name', 'email', 'contact_number', 'area_of_interest', 'primary_mode')


class CourseForm(forms.Form):
    class Meta:
        model = Course
