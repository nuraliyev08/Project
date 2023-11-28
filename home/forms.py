from home.models import Student, Teacher, Admin
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return user


class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        admin.save()
        return user
