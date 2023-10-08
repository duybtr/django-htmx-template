from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django import forms
from django.forms import modelform_factory
from .models import Student
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []

def get_student_list(request):
    context = {}
    context['students'] = Student.objects.all()
    return render(request, 'partial/student/student_list.html', context)

def add_student(request):
    context = {'form': StudentForm()}
    return render(request, 'partial/student/add_student.html', context)

def add_student_submit(request):
    context = {}
    form = StudentForm(request.POST)
    context['form'] = form
    if form.is_valid():
        context['student'] = form.save()
    else:
        return render(request, 'partial/student/add_student.html', context)
    return render(request, 'partial/student/student_row.html', context)

def add_student_cancel(request):
    return HttpResponse()

def edit_student(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {}
    context['student'] = student
    context['form'] = StudentForm(initial={
        'first_name':student.first_name,
        'last_name': student.last_name,
        'gender': student.gender,
        'age': student.age,
        'major': student.major
    })
    return render(request, 'student/partial/edit_student.html', context)

def edit_student_submit(request, student_pk):
    return None
def delete_student(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return HttpResponse()
    



