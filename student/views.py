from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.models import Student
from student.forms import AddStudentForm, EditStudentForm, RegistrationForm, SearchStudentForm
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def student_list(request):
    form = SearchStudentForm()
    students = Student.objects.all().order_by('first_name')
    paginator = Paginator(students, 5)  # Show 5 students per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'student/student_list.html', {'students': students, 'form': form, "page_obj": page_obj})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

@login_required
def student_add(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            message = ''
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            enrollment_date = form.cleaned_data['enrollment_date']
            grade = form.cleaned_data['grade']
            
            # Check if student already exists
            student = Student(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, enrollment_date=enrollment_date, grade=grade)
            student.save()
            return render(request, 'student/student_add.html', {'message': 'Student added successfully!'})
    return render(request, 'student/student_add.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    form = EditStudentForm(pk)
    if request.method == 'POST':
        form = EditStudentForm(pk, request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.email = form.cleaned_data['email']
            student.date_of_birth = form.cleaned_data['date_of_birth']
            student.enrollment_date = form.cleaned_data['enrollment_date']
            student.grade = form.cleaned_data['grade']
            student.save()
            return render(request, 'student/student_edit.html', {'message': 'Student updated successfully!', 'student': student})
    return render(request, 'student/student_edit.html', {'form': form})

def student_search(request):
    if request.method == 'POST':
        form = SearchStudentForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'].strip()
            students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query).order_by('first_name')
            return render(request, 'student/student_search.html', {'students': students, 'success': True})
    return render(request, 'student/student_search.html', {'success': False})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'authentication/register.html', {'message': 'User created successfully!'})
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})