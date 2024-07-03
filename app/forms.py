from django import forms
from app.models import Employee

class empForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

        # fields=['name','age','emp_id','department']