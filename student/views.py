from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.models import Student
from student.forms import AddStudentForm
from student.forms import EditStudentForm

# Create your views here.
def student_list(request):
    students = Student.objects.all().order_by('first_name')
    return render(request, 'student/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

def student_add(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            enrollment_date = form.cleaned_data['enrollment_date']
            grade = form.cleaned_data['grade']
            student = Student(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, enrollment_date=enrollment_date, grade=grade)
            student.save()
            return render(request, 'student/student_add.html', {'message': 'Student added successfully!'})
    return render(request, 'student/student_add.html', {'form': form})

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