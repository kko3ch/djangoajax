from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def home(request):
    form = StudentForm()
    context = {'form': form}
    return render(request, 'core/home.html', context)