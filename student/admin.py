from django.contrib import admin
from student.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')

admin.site.register(Student, StudentAdmin)