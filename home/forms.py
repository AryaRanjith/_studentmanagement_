from django import forms
from .models import Student



SUBJECT_CHOICES = [
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('English', 'English'),
]

class StudentForm(forms.ModelForm):
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select)
    mark = forms.IntegerField(required=False)

    class Meta:
        model = Student
        fields = ['name', 'phone', 'email', 'subject', 'mark']

from django import forms
from .models import Teacher1

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher1
        fields = '__all__'  # stores all fields you created


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head', 'num_students']  # fields you want to show in form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name'}),
            'head': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Head of Department'}),
            'num_students': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Students'}),
        }
