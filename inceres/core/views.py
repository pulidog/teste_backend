from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import InputForm
# importe o calculo

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()

    return render_to_response('hw1.html',
            {'form': form}, context_instance=RequestContext(request))


def present_output(form):
    ratio = form.ratio
    s = compute(ratio)
    return HttpResponse('Resposta! sin(%s)=%s' % (ratio, s))

