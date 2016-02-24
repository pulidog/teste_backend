from __future__ import unicode_literals


from django.db import models
from django.forms import ModelForm



class InputForm(ModelForm):
    class Meta:
        model = #o modelo
        fields = ('A','b','w','T',)