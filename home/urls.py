from django.urls import path
from home import views

urlpatterns = [
    path('', views.example, name='example'),
    path('New/', views.New, name='New'),
    path('akar/', views.akar, name='akar'),
    path('carousel/', views.carousel, name='carousel'),
    path('pagination/', views.pagination, name='pagination'),
    path('example2/', views.example2, name='example2'),
    path('search_one/', views.search_one, name='search_one'),
    path('search_product/', views.search_product, name='search_product'),
    path('teacher_panel/', views.teacher_panel, name='teacher_panel'),
    path('register_teacher/', views.register_teacher.as_view(), name='register_teacher'),
    path('register_student/', views.register_student.as_view(), name='register_student'),
    path('student_panel/', views.student_panel, name='student_panel'),
    path('register_admin/', views.register_admin.as_view(), name='register_admin'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('login_form', views.login_form, name='login_form'),
    path('gmail', views.gmail, name='gmail'),
    path('send_message', views.send_message, name='send_message'),
]
