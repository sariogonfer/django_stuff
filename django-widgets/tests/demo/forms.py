from django import forms
from cegfforms import widgets


class TestFieldsForm(forms.Form):
    complete_text_test = forms.CharField(widget=widgets.CompleteTextInput(row='%(1)s a %(2)s es igual a %(3)s',
                                         result_text='%(1)s thru %(2)s = %(3)s \n', type="number"))