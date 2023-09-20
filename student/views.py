from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

def get_student_list(request):
    context = {}
    context['students'] = get_students()
    return render(request, 'partial/student/student_list.html', context)

def get_students():
    students = []
    students.append(Student(first_name='Joe', last_name='Johnson', gender='Male', age=22, major='Art'))
    students.append(Student(first_name='John', last_name='Doe', gender='Male', age=25, major='History'))
    students.append(Student(first_name='James', last_name='Tyler', gender='Male', age=30, major='Digital Art'))
    students.append(Student(first_name='Conrad', last_name='Well', gender='Male', age=27, major='Biology'))
    students.append(Student(first_name='Fred', last_name='Wells', gender='Male', age=25, major='Computer Engineering'))
    students.append(Student(first_name='George', last_name='Benson', gender='Male', age=25, major='Film'))
    students.append(Student(first_name='Jack', last_name='Hugh', gender='Male', age=21, major='Theater'))
    return students