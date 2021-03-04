from django.shortcuts import render, redirect
from django.views import View
from .login import validate_user

class Index(View):
    def get(self, request):
        if validate_user(request):
            return render(request, 'alpen_admin/index.html')
        else:
            return redirect('teacher_login')