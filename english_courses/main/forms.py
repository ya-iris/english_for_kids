from .models import Application, Student, StudentGroup, Lesson, Announcement, Observation, CustomUser
from django.forms import ModelForm, TextInput, NumberInput, Textarea


class CreateGroupForm(ModelForm):
    class Meta:
        model = StudentGroup
        fields = ["year", "name"]

        widgets = {
            "year": NumberInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the year of studies"
            }),
            "name": TextInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the group name"
            }),
        }


class EditGroupForm(ModelForm):
    class Meta:
        model = StudentGroup
        fields = ["year", "name"]
        widgets = {
            "year": NumberInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the year of studies"
            }),
            "name": TextInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the group name"
            }),
        }


class CreateLessonForm(ModelForm):
    class Meta:
        model = Lesson
        exclude = ("created_at", "student_group")
        fields = ["task"]
        widgets = {
            "task": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the task"
            }),
        }


class EditLessonForm(ModelForm):
    class Meta:
        model = Lesson
        exclude = ("created_at", "group")
        fields = ["task"]
        widgets = {
            "task": Textarea(attrs={
                'id': 'edit-lesson-task',
                'class': 'modal-form__input',
                'placeholder': "Enter the task"
            }),
        }