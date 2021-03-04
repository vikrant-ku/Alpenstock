from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from admins.models.professor import Teacher, Role
from library.models import Issue_book


class Index(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Teacher, username = username)
        try:
            teacher_role = Role.objects.get(user=user)
        except:
            teacher_role = None
        if teacher_role is not None and teacher_role.role == "Librarian":
            return redirect('teacher_login')
        data = {'user':user}
        if teacher_role is not None:
            data['role']= teacher_role
        return render(request, 'teachers/index.html', data)


class Issue_books(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Teacher, username=username)
        issue_books = Issue_book.objects.filter(teacher= user.id)
        data = {'all_issue_book': issue_books}
        return render(request, 'teachers/all-issue-book.html', data)





def validate_user(request):
    username = request.session.get('user')
    if 'TE' not in username:
        return redirect('login')
    else:
        user = get_object_or_404(Teacher, username=username)
        try:
            teacher_role = Role.objects.get(user=user)
        except:
            teacher_role = None
        if teacher_role is not None and teacher_role.role == "Librarian":
            return redirect('teacher_login')
        elif teacher_role is not None and teacher_role.role == "admin" or teacher_role is not None and teacher_role.role == "Admin":
            return redirect('teacher_login')