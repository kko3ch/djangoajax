from django import forms
from .models import Student
from django.forms import fields
from django.forms.models import ModelForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']