from django.urls import path
from .views.index import Index, Issue_books
from .views.event import Events, All_notice, Apply_leave, View_leave, Students_leave, student_leave_status
from .views.login import Login, Change_password
from admins.middleware.auth import auth_middleware




urlpatterns = [
    path('', auth_middleware(Index.as_view()) , name= "teacher_home"),
    path('login/', Login.as_view() , name= "teacher_login"),
    path('change_password/', Change_password.as_view() , name= "teacher_change_password"),
    path('view_issue_books', Issue_books.as_view(), name="issue_books"),


    #event
    path('events/', auth_middleware(Events.as_view()) , name= "teacher_event"),
    path('notice/', auth_middleware(All_notice.as_view()) , name= "teacher_notice"),

    path('apply_leave/', auth_middleware(Apply_leave.as_view()), name='teacher_apply_leave'),
    path('view_leave/', auth_middleware(View_leave.as_view()), name='teacher_view_leave'),
    path('students_leave/', auth_middleware(Students_leave.as_view()), name='teacher_students_leave'),
    path('students_leave/<int:pk>/<str:status>/', auth_middleware(student_leave_status.as_view()), name='teacher_students_leave_status'),


    # path("students_leave", auth_middleware())


]