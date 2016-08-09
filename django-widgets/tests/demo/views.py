from .forms import TestFieldsForm
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    form = TestFieldsForm()

    last_result = request.POST.get('complete_text_test', '')

    return render_to_response('demo/index.html', {'form': form, 'last_result': last_result}, content_type=RequestContext(request))