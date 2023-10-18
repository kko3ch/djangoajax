from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = StudentForm()
    student = Student.objects.all()
    context = {'form': form, 'student': student}
    return render(request, 'core/home.html', context)

@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            course = request.POST['course']

            s = Student(name=name, email=email, course=course)
            s.save()
            stu = Student.objects.values()
            student_data = list(stu)

            return JsonResponse({'status': 'Data Saved', 'student_data': student_data})
        
        else: 
            return JsonResponse({'status': 'Unable To Save'})

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        st = Student.objects.get(pk=id)
        st.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})