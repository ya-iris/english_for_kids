from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.models import Group

from .models import Application, Student, StudentGroup, Lesson, Announcement, Observation, CustomUser
from django.forms import ModelForm, TextInput, Textarea, EmailInput, Select, ModelChoiceField, \
    NumberInput, CharField, EmailField, PasswordInput


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


class CreateObservationForm(ModelForm):
    class Meta:
        model = Observation
        exclude = ("created_at", "student")
        fields = ["observation"]
        widgets = {
            "observation": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter an observation"
            }),
        }


class EditObservationForm(ModelForm):
    class Meta:
        model = Observation
        exclude = ("created_at", "student")
        fields = ["observation"]
        widgets = {
            "observation": Textarea(attrs={
                'id': 'edit-observation',
                'class': 'modal-form__input',
                'placeholder': "Enter an observation"
            }),

        }


class CreateAnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        exclude = ("created_at",)
        fields = ["announcement"]
        widgets = {
            "announcement": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the announcement"
            }),
        }


class EditAnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        exclude = ("created_at",)
        fields = ["announcement"]
        widgets = {
            "announcement": Textarea(attrs={
                'id': 'edit-announcement',
                'class': 'modal-form__input',
                'placeholder': "Enter the announcement"
            }),
        }


class CreateApplicationForm(ModelForm):

    def clean_f_name(self):
        f_name = self.cleaned_data["f_name"]

        if not f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return f_name

    def clean_l_name(self):
        l_name = self.cleaned_data["l_name"]

        if not l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return l_name

    def clean_parent_tel_numb(self):
        parent_tel_numb = self.cleaned_data["parent_tel_numb"]

        if not parent_tel_numb.isdecimal():
            raise ValidationError("Phone number should only contain digits")
        return parent_tel_numb

    def clean_parent_f_name(self):
        parent_f_name = self.cleaned_data["parent_f_name"]

        if not parent_f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return parent_f_name

    def clean_parent_patronimic(self):
        parent_patronimic = self.cleaned_data["parent_patronimic"]

        if len(parent_patronimic) > 0:
            if not parent_patronimic.isalpha():
                raise ValidationError("The patronymic should only contain letters")
        return parent_patronimic

    def clean_parent_l_name(self):
        parent_l_name = self.cleaned_data["parent_l_name"]

        if not parent_l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return parent_l_name

    class Meta:

        model = Application
        exclude = ('created_at',)
        fields = ["f_name", "l_name", "age", "parent_tel_numb", "parent_email", "parent_f_name",
                  "parent_patronimic", "parent_l_name"]

        widgets = {
            "f_name": TextInput(attrs={
                'class': 'form__input',
                'label': "Child's first name"
            }),

            "l_name": TextInput(attrs={
                'class': 'form__input',
                'label': "Child's last name"
            }),

            "age": NumberInput(attrs={
                'class': 'form__input',
                'label': "Child's age"
            }),

            "parent_f_name": TextInput(attrs={
                'class': 'form__input',
                'label': "Parent's first name"
            }),

            "parent_patronimic": TextInput(attrs={
                'class': 'form__input',
                'label': "Parent's patronymic"
            }),

            "parent_l_name": TextInput(attrs={
                'class': 'form__input',
                'label': "Parent's last name"
            }),

            "parent_tel_numb": TextInput(attrs={
                'class': 'form__input',
                'label': "Parent's phone number",
                'minlength': 10
            }),

            "parent_email": EmailInput(attrs={
                'class': 'form__input',
                'label': "Parent's e-mail"
            })
        }


class CreateStudentForm(UserCreationForm):
    username = CharField(max_length=20, label="Username", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter a username"
    }))
    first_name = CharField(max_length=20, label="First name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the student's first name",
        'id': "student-first-name"
    }))
    last_name = CharField(max_length=30, label="Last name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the student's last name",
        'id': "student-last-name"
    }))
    email = EmailField(max_length=200, label="E-mail", widget=EmailInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's e-mail address",
        'id': "student-email"
    }))
    parent_f_name = CharField(max_length=20, label="Parent's first name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's first name",
        'id': "parent-first-name"
    }))
    parent_patronimic = CharField(max_length=30, label="Parent's patronymic", required=False,
                                  help_text="Parent's patronymic can be omitted", widget=TextInput(attrs={
            'class': 'modal-form__input',
            'placeholder': "Enter the parent's patronymic",
            'id': "parent-patronymic"
        }))
    parent_l_name = CharField(max_length=30, label="Parent's last name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's last name",
        'id': "parent-last-name"
    }))
    parent_tel_numb = CharField(max_length=10, min_length=10, label="Parent's phone number",
                                widget=TextInput(attrs={
                                    'class': 'modal-form__input',
                                    'placeholder': "Enter the parent's phone number",
                                    'id': "phone-number"
                                }))

    student_group = ModelChoiceField(queryset=StudentGroup.objects.all(), label="Student group",
                                     required=False, help_text="Student's group can be omitted",
                                     widget=Select(attrs={
                                         'class': 'select-group',
                                         'placeholder': "Choose the student's groups"
                                     }))

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]

        if not first_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]

        if not last_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return last_name

    def clean_parent_tel_numb(self):
        parent_tel_numb = self.cleaned_data["parent_tel_numb"]

        if not parent_tel_numb.isdecimal():
            raise ValidationError("Phone number should only contain digits")
        return parent_tel_numb

    def clean_parent_f_name(self):
        parent_f_name = self.cleaned_data["parent_f_name"]

        if not parent_f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return parent_f_name

    def clean_parent_patronimic(self):
        parent_patronimic = self.cleaned_data["parent_patronimic"]

        if len(parent_patronimic) > 0:
            if not parent_patronimic.isalpha():
                raise ValidationError("The patronymic should only contain letters")
        return parent_patronimic

    def clean_parent_l_name(self):
        parent_l_name = self.cleaned_data["parent_l_name"]

        if not parent_l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return parent_l_name

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'parent_f_name', 'parent_patronimic', 'parent_l_name',
                  'parent_tel_numb', 'student_group')

    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
        self.fields.pop('password2')

    @transaction.atomic
    def save(self, pword):
        self.cleaned_data['password1'] = pword
        user = super().save()
        group = Group.objects.get(name='student')
        user.groups.add(group)
        user.save()

        student = Student.objects.create(user=user)
        student.parent_f_name = self.cleaned_data.get('parent_f_name')
        student.parent_patronimic = self.cleaned_data.get('parent_patronimic')
        student.parent_l_name = self.cleaned_data.get('parent_l_name')
        student.parent_tel_numb = self.cleaned_data.get('parent_tel_numb')
        student.student_group = self.cleaned_data.get('student_group')
        student.save()
        return user


class EditUserForm(ModelForm):
    username = CharField(max_length=20, label="Username", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter a username"
    }))
    first_name = CharField(max_length=20, label="First name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the student's first name"
    }))
    last_name = CharField(max_length=30, label="Last name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the student's last name"
    }))
    email = EmailField(max_length=200, label="E-mail", widget=EmailInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's e-mail address"
    }))

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]

        if not first_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]

        if not last_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return last_name

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


class EditStudentForm(ModelForm):
    parent_f_name = CharField(max_length=20, label="Parent's first name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's first name"
    }))
    parent_patronimic = CharField(max_length=30, label="Parent's patronymic", required=False,
                                  help_text="Parent's patronymic can be omitted", widget=TextInput(attrs={
            'class': 'modal-form__input',
            'placeholder': "Enter the parent's patronymic"
        }))
    parent_l_name = CharField(max_length=30, label="Parent's last name", widget=TextInput(attrs={
        'class': 'modal-form__input',
        'placeholder': "Enter the parent's last name"
    }))
    parent_tel_numb = CharField(max_length=10, min_length=10, label="Parent's phone number",
                                widget=TextInput(attrs={
                                    'class': 'modal-form__input',
                                    'placeholder': "Enter the parent's phone number"
                                }))

    student_group = ModelChoiceField(queryset=StudentGroup.objects.all(), label="Student group",
                                     required=False, help_text="Student's group can be omitted",
                                     widget=Select(attrs={
                                         'class': 'select-group',
                                         'placeholder': "Choose the student's groups"
                                     }))

    def clean_parent_tel_numb(self):
        parent_tel_numb = self.cleaned_data["parent_tel_numb"]

        if not parent_tel_numb.isdecimal():
            raise ValidationError("Phone number should only contain digits")
        return parent_tel_numb

    def clean_parent_f_name(self):
        parent_f_name = self.cleaned_data["parent_f_name"]

        if not parent_f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return parent_f_name

    def clean_parent_patronimic(self):
        parent_patronimic = self.cleaned_data["parent_patronimic"]

        if len(parent_patronimic) > 0:
            if not parent_patronimic.isalpha():
                raise ValidationError("The patronymic should only contain letters")
        return parent_patronimic

    def clean_parent_l_name(self):
        parent_l_name = self.cleaned_data["parent_l_name"]

        if not parent_l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return parent_l_name

    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ('parent_f_name', 'parent_patronimic', 'parent_l_name',
                  'parent_tel_numb', 'student_group')


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    username = CharField(widget=TextInput(
        attrs={'class': 'form__input',
               'id': 'email'
               }))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form__input',
            'id': 'password',
            'minlength': 10,
            'maxlength': 10
        }))
