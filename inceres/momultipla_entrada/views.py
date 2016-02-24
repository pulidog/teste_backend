from django.shortcuts import render_to_response
from django.template import RequestContext
from models import InputForm
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
            result = result.replace('static/', '')
    else:
        form = InputForm()

    return render_to_response('multipla.html',
            {'form': form,
             'result': result,
             }, context_instance=RequestContext(request))