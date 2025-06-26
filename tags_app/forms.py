from django import forms 
from.models import Subscriber

class unsubform(forms.Modelform):
    class Meta:
        model = Subscriber
        fields= ['email']