from django.contrib import admin
from .models.students import Students
from .models.professor import Teacher, Role
from .models.classes import Class, Class_subjects
from .models.notice import Notices
from .models.leave import Leave
from .models.staff import Staff

class Student_Admin(admin.ModelAdmin):
    list_display = ('username', 'admission_no', 'first_name', 'class_name','section', )
    list_filter = ('class_name', 'section')
    search_fields = ['username', 'admission_no','first_name', 'last_name',]
    # list_editable = ('lable', 'type')

class Teacher_Admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','work_shift', )
    list_filter = ('work_shift',)
    search_fields = ['username','first_name', 'last_name',]

class Notice_Admin(admin.ModelAdmin):
    list_display = ('recipient', 'type', 'date')
    list_filter = ('recipient', 'type', 'date')
    search_fields = ['recipient', 'type', ]

class Subject_Admin(admin.ModelAdmin):
    list_display = ('class_name', 'section')
    list_filter = ('class_name', 'section')

class Leave_admin(admin.ModelAdmin):

    list_display = ('type','teacher', 'student', 'start_date', 'end_date', 'halfday', 'status', 'is_teacher', 'is_student')
    list_filter = ('halfday', 'status', 'is_teacher', 'is_student')



admin.site.register(Students, Student_Admin)
admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Staff)
admin.site.register(Class)
admin.site.register(Class_subjects, Subject_Admin)
admin.site.register(Role)
admin.site.register(Leave, Leave_admin)
admin.site.register(Notices, Notice_Admin)


