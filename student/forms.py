from django import forms
import re
from django.core.exceptions import ValidationError
from student.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def validate_email(value):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, value):
        raise ValidationError("Please enter a valid email address.")

def validate_spaces(value):
    if value.strip() == '':
        raise ValidationError("This field cannot be empty.")

class AddStudentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(
        label='Email', 
        max_length=100,
        validators=[validate_email],
    )
    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.SelectDateWidget(years=range(1990, 2025)),
    )
    enrollment_date = forms.DateField(
        label='Enrollment Date',
        widget=forms.SelectDateWidget(years=range(1990, 2025)),
    )
    grade = forms.IntegerField(
        label='Grade', 
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 13)]),
    )

class EditStudentForm(forms.Form):
    def __init__(self,pk,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # get the student object
        student = Student.objects.get(pk=pk)

        # set initial values
        if student:
            self.fields['first_name'].initial = student.first_name
            self.fields['last_name'].initial = student.last_name
            self.fields['email'].initial = student.email
            self.fields['date_of_birth'].initial = student.date_of_birth
            self.fields['enrollment_date'].initial = student.enrollment_date
            self.fields['grade'].initial = student.grade

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(
        label='Email', 
        max_length=100,
        validators=[validate_email],
    )
    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.SelectDateWidget(years=range(1990, 2025)),
    )
    enrollment_date = forms.DateField(
        label='Enrollment Date',
        widget=forms.SelectDateWidget(years=range(1990, 2025)),
    )
    grade = forms.IntegerField(
        label='Grade', 
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 13)]),
    )

class SearchStudentForm(forms.Form):
    query = forms.CharField(
        label='Search Query',
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search for Student by Name", "style": "width: 200px;"}
        ),
        validators=[validate_spaces],
    )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']