from __future__ import unicode_literals


# Create your models here.


from django.db import models
from django.forms import ModelForm



class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ('ratio',)