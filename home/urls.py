from django.urls import path
from . import views
from .views import student_list, add_student,teacher_list


urlpatterns = [
    path('', views.login_home, name='login_home'),
    path('admin-login/', views.admin_login, name='admin_login'),
# path('admin-home/', views.admin_home, name='admin_home'),
# path('admin-register/', views.admin_register, name='admin_register'),

# path('teacher-login/', views.teacher_login, name='teacher_login'),
# path('student-login/', views.student_login, name='student_login'),

    path('add-student-user/', views.add_student_user, name='add_student_user'),

    path('students/', student_list, name='student_list'),
    # path('', lambda request: redirect('student_list')),  # 👈 add this line

    path('add-student/', add_student, name='add_student'),

    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
        path('add-teacher-user/', views.add_teacher_user, name='add_teacher_user'),

     path('teachers/',views.teacher_list, name='teacher_list'),
     
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('edit-teacher/<int:pk>/', views.edit_teacher, name='edit_teacher'),
     path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('departments/delete/<int:pk>/', views.delete_department, name='delete_department'),
    # Student login
     path('studentss/', views.student_auth, name='student_login'),
    path('students/home/', views.student_home, name='student_home'),
    # Teacher login
    path('teacherss/',views.teacher_auth,name = "teacher_login"),
    path('teacher/home',views.teacher_home,name = "teacher_home"),
    path('teacher/add-marks', views.add_marks, name="add_marks"),
    path('teacher/add-attendance', views.teacher_attendance, name='add_attendance'),
    path("student/marks", views.student_view_marks, name="student_marks"),
    path('student/attendance', views.student_attendance, name='student_attendance'),
    path("student/leave/", views.apply_leave, name="apply_leave"),
path("teacher/leaves/", views.teacher_leave_list, name="teacher_leave_list"),
path("teacher/leave/update/<int:id>/", views.update_leave_status, name="update_leave_status"),




]

    