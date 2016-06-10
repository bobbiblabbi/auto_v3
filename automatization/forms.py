# coding=utf-8
from django import forms
from automatization.models import *


class PagesForm(forms.ModelForm):
    class Meta:
        model = Template
        exclude = []

class CoordinateForm1(forms.ModelForm):
    class Meta:
        model = Page1
        exclude = []

