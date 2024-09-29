from django.shortcuts import render
from student.models import Student

# Create your views here.
def student_list(request):
    students = Student.objects.all().order_by('first_name')
    return render(request, 'student/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

def student_add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        enrollment_date = request.POST['enrollment_date']
        grade = request.POST['grade']
        student = Student(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, enrollment_date=enrollment_date, grade=grade)
        student.save()
        return render(request, 'student/student_add.html', {'message': 'Student added successfully!'})
    return render(request, 'student/student_add.html')

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.date_of_birth = request.POST['date_of_birth']
        student.enrollment_date = request.POST['enrollment_date']
        student.grade = request.POST['grade']
        student.save()
        return render(request, 'student/student_edit.html', {'message': 'Student updated successfully!'})
    return render(request, 'student/student_edit.html', {'student': student})