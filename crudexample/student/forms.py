from django import forms  
from .models import stud_record

class stud_record_form(forms.ModelForm):
    class Meta:
        model = stud_record
        fields = "__all__"