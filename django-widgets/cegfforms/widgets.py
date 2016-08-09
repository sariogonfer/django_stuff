from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django import forms
import re


class CompleteTextInput(forms.TextInput):
    template_name = 'cegfforms/complete_text_input.html'

    def __init__(self, row=None, init_rows=None, max_rows=None, result_text=None, attrs=None, type="text"):
        self.__row = row if row is not None else '%(1)s'
        self.__init_rows = init_rows if init_rows is not None else 2
        self.__max_rows = max_rows if max_rows is not None else 3
        self.__result_text = result_text if result_text is not None else '%(1)s'
        self.__replace_dict = {}
        self.__input_html = '<input type="%s">' % type
        self.__attrs = attrs

        super(CompleteTextInput, self).__init__(attrs)
        l = re.findall(r'%\([a-zA-Z_0-9]*\)s', self.__row)
        for foo in set(l):
            aux = self.__input_html.replace(">", " tag='%s'>" % foo)
            self.__replace_dict[foo[2:-2]] = aux

        print self.__replace_dict

    class Media:
        js = (
            'cegfforms/js/complete_text_input.js',
        )

    def render(self, name, value, attrs={}):
        context = {
            'init_rows': range(self.__init_rows),
            'max_rows': self.__max_rows,
            'row': self.__row % self.__replace_dict,
            'result_text': self.__result_text.encode('string_escape'),
            'attrs': dict(self.__attrs.items() + attrs.items()),
            'name': name
        }
        return mark_safe(render_to_string(self.template_name, context))

    def value_from_datadict(self, data, files, name):
        return data[name].decode('unicode_escape')
