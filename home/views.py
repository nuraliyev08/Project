from django.shortcuts import render, redirect
from home.forms import StudentSignUpForm, TeacherSignUpForm, AdminSignUpForm
from home.models import News, Akar, Carousel, Phone, Category,  Search, Student, Teacher, Admin
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail


def example(request):
    return render(request, 'firs_page.html')


def New(request):
    new = News.objects.all()
    context = {
        'new': new,
    }
    return render(request, 'ckeditor.html', context)


#####################################################################################################
def akar(request):
    akar = Akar.objects.all()
    context = {
        'akar': akar,
    }
    return render(request, 'akar.html', context)
#####################################################################################################
def carousel(request):
    carousel = Carousel.objects.all()
    context = {
        'carousel': carousel
    }
    return render(request, 'carousel.html', context)

#####################################################################################################
def pagination(request):
     pagination = Phone.objects.all()
     paginator = Paginator(pagination, 1)
     page_request_var = 'page'
     page = request.GET.get(page_request_var)
     try:
         pagination = paginator.page(page)
     except PageNotAnInteger:
         pagination = paginator.page(1)
     except EmptyPage:
         pagination = paginator.page(paginator.num_pages)
     context = {
         'pagination': pagination
     }
     return render (request, 'pagination.html', context)
#####################################################################################################
def example2(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'chart.html', context)
#####################################################################################################

def search_one(request):
    return render(request, 'search.html')





def search_product(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Search.objects.filter(title__contains=searched)
        context = {
            'searched': searched,
            'product': product,
        }
        return render(request, 'search.html', context)


#####################################################################################################
class register_student(CreateView):
    template_name = 'register_student.html'
    form_class = StudentSignUpForm
    success_url = reverse_lazy('student_panel')
    success_message = "Вы успешно зарегистрировались"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

class register_teacher(CreateView):
    template_name = 'register_teacher.html'
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('teacher_panel')
    success_message = "Вы успешно зарегистрировались"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid



def student_panel(request):
    try:
        student = Student.objects.get(user=request.user)
    except:
        return redirect('register_student')
    context = {
        'student':student,
    }
    return render(request, 'student.html', context)


def teacher_panel(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except:
        return redirect('register_teacher')
    context = {
        'teacher':teacher,
    }
    return render(request, 'teacher.html', context)




class register_admin(CreateView):
    template_name = 'register_admin.html'
    form_class = AdminSignUpForm
    success_url = reverse_lazy('admin_panel')
    success_message = "Вы успешно зарегистрировались"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

def admin_panel(request):
    try:
        admin = Admin.objects.get(user=request.user)
    except:
        return redirect('register_admin')
    context = {
        'admin': admin,
    }
    return render(request, 'admin.html', context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Admin.objects.get(user_id=request.user.id)
                return redirect('admin.panel')
            except:
                try:
                    Student.objects.get(user_id=request.user.id)
                    return redirect('student_panel')
                except:
                    try:
                        Teacher.objects.get(user_id=request.user.id)
                        return redirect('teacher_panel')
                    except:
                        return redirect('login_form')
                else:
                    return redirect('login_form')
                return render(request, 'login.html')


def gmail(request):
    return render(request, 'gmail.html')

def send_message(request):
    if request.method =='POST':
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Yangi xabar',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        return redirect('gmail')

