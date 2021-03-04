from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from admins.models.students import Students
from admins.models.professor import Teacher



class Login(View):
    def get(self, request):
        is_student = True
        data = {'is_student':is_student}
        return render(request, 'alpen_admin/login.html', data)


    def post(self, request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = None
        if "ST" in username:
            try:
                user = Students.objects.get(username=username)

            except:
                messages.error(request, "User dose'nt Exist")

        if user is not None:
            flag = check_password(password, user.password)
            if flag:

                request.session['user'] = user.username
                request.session['name'] = user.first_name
                return redirect('student_home')
            else:
                messages.error(request, "Password Do not match")
        else:
            messages.error(request, 'Please check username')
        return redirect("login")

class Logout(View):
    def get(self, request):
        username = request.session.pop('user')
        name = request.session.pop('name')
        messages.success(request, f"{username} successfully logout ")
        return redirect('login')


class Change_password(View):
    def get(self, request):
        return render(request, "teachers/change_password.html")
    def post(self, request):
        old_pass = request.POST.get('old_pass')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            username = request.session.get('user')
            user = get_object_or_404(Students, username=username)
            flag = check_password(old_pass, user.password)
            if flag:
                user.password = make_password(pass1)
                user.save()
            else:
                messages.error(request, 'Please Check Your Password')
        else:
            messages.error(request, "New Password and Confirm Password Do not Match !")
        return redirect('change_password')








