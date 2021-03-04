from django.urls import path
from .views.login import Login, Logout, Change_password
from .views.index import Index, Issue_books
from .views.events import All_notice, Events, Apply_leave, All_leaves



urlpatterns = [
    path('', Index.as_view() , name= "student_home"),
    path('login/', Login.as_view() , name= "login"),
    path('change_password/', Change_password.as_view() , name= "change_password"),
    path('logout/', Logout.as_view() , name= "logout"),
    path('view_issue_books',Issue_books.as_view(), name='issue_books' ),


    #notice
    path('events/', Events.as_view(), name='student_events'),
    path('notice/', All_notice.as_view() , name= "student_notice"),
    path('apply_leave', Apply_leave.as_view(), name="apply_leave" ),
    path('view_leave', All_leaves.as_view(), name="view_leave" ),


]