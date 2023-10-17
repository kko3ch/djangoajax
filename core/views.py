from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def home(request):
    form = StudentForm()
    student = Student.objects.all()
    context = {'form': form, 'student': student}
    return render(request, 'core/home.html', context)