from .views.index import Index
from .views.student import Add_students, All_students , Delete_student, Edit_student
from .views.professor import Add_professors , All_professor , Edit_professor, Delete_professor, Assign_role, teacher_leave, teacher_leave_status
from .views.staff import Add_staff, All_staff, delete_staff, Edit_staff
from .views.login import Reset_password
from .views.events import Events, Add_notice, All_notice, Delete_notice, temp
from .views.classes import Add_class, All_class
from .views.subject import Add_subjects, All_subjects
from django.urls import path
from .middleware.auth import auth_middleware



urlpatterns = [

    path('', auth_middleware(Index.as_view()), name="admin_home"),
    path('reset_password/', auth_middleware(Reset_password.as_view()), name="reset_password"),



    #students
    path('add_student/', auth_middleware(Add_students.as_view()), name="add_students"),
    path('all_students/', auth_middleware(All_students.as_view()), name='admin_all_students'),
    path('delete_student/<int:pk>/', auth_middleware(Delete_student.as_view()), name='all_students'),
    path('edit_student/<int:pk>/', auth_middleware(Edit_student.as_view()), name="edit_student"),

    #Teachers
    path('add_teachers/', Add_professors.as_view(), name="add_teacher"),
    path('all_teachers/', auth_middleware(All_professor.as_view()), name='all_teachers'),
    path('delete_teacher/<int:pk>/', auth_middleware(Delete_professor.as_view()), name='delete_teachers'),
    path('edit_teacher/<int:pk>/', auth_middleware(Edit_professor.as_view()), name="edit_teacher"),
    path('assign_role/<int:pk>/', auth_middleware(Assign_role.as_view()), name='assign_role'),
    path('leaves/', auth_middleware(teacher_leave.as_view()), name='teachers_leave'),
    path('leave_status/<int:pk>/<str:status>/', auth_middleware(teacher_leave_status.as_view()), name='teacher_leave_status'),

    #staff
    path('add_staff/', auth_middleware(Add_staff.as_view()), name='add_staff'),
    path('all_staff/', auth_middleware(All_staff.as_view()), name='all_staff'),
    path('delete_staff/<int:pk>/', auth_middleware(delete_staff.as_view()), name='delete_staff'),
    path('edit_staff/<int:pk>/<str:first_name>/', auth_middleware(Edit_staff.as_view()), name='edit_staff'),


    #events
    path('events/', Events.as_view(), name='events'),
    path('add_notice/', Add_notice.as_view(), name='add_notice'),
    path('notice/', All_notice.as_view(), name='admin_notice'),
    path('delete_notice/<int:pk>/', Delete_notice.as_view(), name='delete_notice'),

    path('temp/', temp.as_view(), name='temp'),

    #class
    path('add_class/', Add_class.as_view(), name='add_class'),
    path('all_class/', All_class.as_view(), name='all_class'),


    #subjects
    path('add_subjects/', Add_subjects.as_view(), name='add_subjects'),
    path('all_subjects/', All_subjects.as_view(), name='all_subjects'),




]





