from django.urls import path
from .views.books import Add_books, All_books, Edit_book, Delete_book, Issue_books, search_user, All_issue_book
from .views.index import Index, Apply_leave,View_leave, All_notice
from admins.middleware.auth import auth_middleware




urlpatterns = [
    path('', auth_middleware(Index.as_view()) , name= "library_index"),
    path('apply_leave/', auth_middleware(Apply_leave.as_view()) , name= "library_apply_leave"),
    path('view_leave/', auth_middleware(View_leave.as_view()) , name= "library_view_leave"),
    path('notice/', auth_middleware(All_notice.as_view()) , name= "library_notice"),


    #books
    path('add_books/', auth_middleware(Add_books.as_view()) , name= "add_books"),
    path('all_books/', auth_middleware(All_books.as_view()) , name= "all_books"),
    path('edit_book/<int:pk>/', auth_middleware(Edit_book.as_view()) , name= "edit_book"),
    path('delete_book/<int:pk>/', auth_middleware(Delete_book.as_view()) , name= "delete_book"),
    path('issue_book/', auth_middleware(Issue_books.as_view()) , name= "issue_book"),
    path('all_issue_books/', auth_middleware(All_issue_book.as_view()) , name= "all_issue_book"),
    path('user/', auth_middleware(search_user), name='search_user'),

]