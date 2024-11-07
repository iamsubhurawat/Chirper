from django import forms
from .models import student, course

class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = [
            "id",
            "name",
            "age",
            "course",
            "image",
        ]

class course_form(forms.ModelForm):
    class Meta:
        model = course
        fields = [
            "id",
            "name",
        ]

class search_student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = [
            'name',
        ]