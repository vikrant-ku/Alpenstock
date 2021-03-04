from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from admins.models.students import Students
from django.contrib import messages
from library.models import Issue_book

class Index(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        if  'ST' in username:
            user = get_object_or_404(Students, username = username)
            data = {'user':user}
            return render(request, 'students/index.html', data)
        else:
            return redirect('login')

class Issue_books(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Students, username=username)
        issue_books = Issue_book.objects.filter(student= user.id)
        data = {'all_issue_book': issue_books}
        return render(request, 'students/all-issue-book.html', data)



def validate_user(request):
    username = request.session.get('user')
    if 'ST' not in username:
        return redirect('login')
