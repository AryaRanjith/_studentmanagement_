from django.db import models
from django.contrib.auth.models import User

class StudentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,       # 👈 TEMPORARY
        blank=True
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    mark = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class TeacherUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Teacher1(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,        # 👈 TEMPORARY (IMPORTANT)
        blank=True
    )

    teacher_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


    
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)  # unique ID for each department
    name = models.CharField(max_length=100)            # Department Name
    head = models.CharField(max_length=100, blank=True) # Head of Department (optional)
    num_students = models.IntegerField(default=0)      # Number of students

    def __str__(self):
        return self.name

# at teacher dashboard to add marks  
class Marks(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="marks")
    subject = models.CharField(max_length=100)
    mark = models.IntegerField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="uploaded_marks")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.subject} : {self.mark}"
    
class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance_records")
    subject = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subject_attendance") 
    status = models.CharField(max_length=10, choices=[("Present","Present"),("Absent","Absent")])
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="uploaded_attendance")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.subject.name} - {self.status}"
    
class Leave(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'   # ✅ FIX HERE
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_leaves"
    )
    review_comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.status}"
