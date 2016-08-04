from django import forms
from .widgets import CompleteTextInput

__all__ = ('CompleteTextField')


class CompleteTextField(forms.Field):
    widget = CompleteTextInput
