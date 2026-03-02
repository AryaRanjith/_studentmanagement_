from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='admin_login')
def add_student_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            user = User.objects.create_user(username=username, password=password)
            # optional: create StudentUser object
            StudentUser.objects.create(user=user)

            messages.success(request, f"Student '{username}' added successfully!")

        return redirect('add_student_user')

    return render(request, 'home/add_student_user.html')

@login_required(login_url='admin_login')
def admin_home(request):
    return render(request, 'home/admin_login.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, "Invalid admin credentials!")

    return render(request, 'home/admin_login.html')


def login_home(request):
    return render(request, 'home/login_home.html')


def student_list(request):
    return render(request, 'home/student_list.html')
def add_student(request):
    return render(request, 'home/add_student.html')
def edit_student(request):
    return render(request, 'home/edit_student.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student,Marks,StudentUser,TeacherUser
from .forms import StudentForm

@login_required(login_url='admin_login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'home/student_list.html', {'students': students})

@login_required(login_url='admin_login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'home/add_student.html', {'form': form})

@login_required(login_url='admin_login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'home/edit_student.html', {'form': form})

from .forms import TeacherForm 
from .models import Teacher1

@login_required(login_url='admin_login')
def add_teacher_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            user = User.objects.create_user(username=username, password=password)
            # optional: create TeacherUser object
            TeacherUser.objects.create(user=user)

            messages.success(request, f"Teacher '{username}' added successfully!")

        return redirect('add_teacher_user')

    return render(request, 'home/add_teacher_user.html')

@login_required(login_url='admin_login')
def teacher_list(request):
    teachers = Teacher1.objects.all()  # ✔ fetch ALL teachers as list
    return render(request, 'home/teachers_list.html', {'teachers': teachers})

@login_required(login_url='admin_login')
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)   # Don't save confirm_password
            teacher.password = form.cleaned_data['password']  # Take only password
            teacher.save()   # Now save to DB
            return redirect('teacher_list')
    else:
        form = TeacherForm()

    return render(request, 'home/add_teacher.html', {'form': form})

@login_required(login_url='admin_login')
def edit_teacher(request, pk):
    teacher = Teacher1.objects.get(id=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'home/edit_teacher.html', {'form': form})

from .models import Department,Attendance
from .forms import DepartmentForm

# List all departments
@login_required(login_url='admin_login')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'home/department_list.html', {'departments': departments})

# Add a new department
@login_required(login_url='admin_login')
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'home/add_department.html', {'form': form})

# Edit an existing department
@login_required(login_url='admin_login')
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'home/edit_department.html', {'form': form})

# Delete a department
@login_required(login_url='admin_login')
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'home/delete_department.html', {'department': department})

# ===================Student Login============================

def student_auth(request):
    if request.method == "POST":

        # signup logic
        if "signup" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            pass1 = request.POST.get("password1")
            pass2 = request.POST.get("password2")

            if pass1 != pass2:
                messages.error(request, "Passwords do not match!")
            else:
                User.objects.create_user(username=username, email=email, password=pass1)
                messages.success(request, "Registration successful! Now login.")
                return redirect("student_login")

        # login logic
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("student_home")
            else:
                messages.error(request, "Invalid login details!")

    return render(request, "home/student_login.html")

def student_home(request):
    return render(request,'home/student_home.html')

def teacher_auth(request):
    if request.method == "POST":

        # Signup logic
        if "signup" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            pass1 = request.POST.get("password1")
            pass2 = request.POST.get("password2")

            if pass1 != pass2:
                messages.error(request, "Passwords do not match!")
            else:
                User.objects.create_user(username=username, email=email, password=pass1)
                messages.success(request, "Registration successful! Now login.")
                return redirect("teacher_login")

        # Login logic
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("teacher_home")
            else:
                messages.error(request, "Invalid login details!")

    return render(request, "home/teacher_login.html")

def teacher_home(request):
    return render(request,'home/teacher_home.html')

@login_required(login_url='/student/login')
def add_marks(request):
    if request.method == "POST":
        student_username = request.POST['student_username']
        subject = request.POST['subject']
        mark = request.POST['mark']

        try:
            student = User.objects.get(username=student_username)
            Marks.objects.create(
                student=student,
                subject=subject,
                mark=mark,
                uploaded_by=request.user
            )
            messages.success(request, "Marks uploaded successfully!")
        except User.DoesNotExist:
            messages.error(request, "Student not found!")

    return render(request, 'home/add_marks.html')


def student_view_marks(request):
    marks = Marks.objects.filter(student=request.user)
    return render(request, "home/student_marks.html", {"marks": marks})

def teacher_attendance(request):
    students = User.objects.all()  # student accounts
    subjects = Department.objects.all()  # subjects dropdown

    if request.method == "POST":
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        status = request.POST.get("status")

        student = User.objects.get(id=student_id)
        subject = Department.objects.get(department_id=subject_id)

        Attendance.objects.create(
            student=student,
            subject=subject,
            status=status,
            uploaded_by=request.user
        )

        messages.success(request, "Attendance added successfully!")
    
    return render(request, "home/teacher_attendance.html", {
        "students": students,
        "subjects": subjects
    })

from .models import Attendance

def student_attendance(request):
    attendances = Attendance.objects.filter(student=request.user).order_by('-date')
    return render(request, "home/student_attendance.html", {
        "attendances": attendances
    })

from .models import Leave

@login_required
def apply_leave(request):
    if request.method == "POST":
        Leave.objects.create(
            student=request.user,
            from_date=request.POST.get("leave_from"),
            to_date=request.POST.get("leave_to"),
            reason=request.POST.get("reason"),
            status="Pending"
        )
        return redirect("apply_leave")

    # ✅ FETCH ALL STATUSES
    leaves = Leave.objects.filter(student=request.user).order_by("-applied_at")

    return render(request, "home/apply_leave.html", {"leaves": leaves})


@login_required
def teacher_leave_list(request):
    leaves = Leave.objects.all().order_by('-applied_at')
    return render(request, 'home/leave_list.html', {'leaves': leaves})

@login_required
def update_leave_status(request, id):
    if request.method == "POST":
        leave = get_object_or_404(Leave, id=id)
        leave.status = request.POST.get('status')  # Pending / Approved / Rejected
        leave.reviewed_by = request.user
        leave.save()

    return redirect('teacher_leave_list')

