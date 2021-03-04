from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from admins.models.professor import Teacher, Role


class Login(View):
    def get(self, request):
        data = {'is_teacher':True}
        return render(request, 'alpen_admin/login.html', data)


    def post(self, request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = None
        if "TE" in username:
            try:
                user = Teacher.objects.get(username=username)

            except:
                messages.error(request, "User dose'nt Exist")

        if user is not None:
            flag = check_password(password, user.password)
            if flag:
                request.session['user'] = user.username
                request.session['name'] = user.first_name
                try:
                    role = Role.objects.get( user = user.id)
                except:
                    role = False
                if role:
                    if role.role == "Librarian":
                        return redirect('library_index')
                    elif role.role == 'admin' or role.role == 'Admin':
                        return redirect('admin_home')
                    else:
                        return redirect('teacher_home')
            else:
                messages.error(request, "Password Do not match")
        else:
            messages.error(request, 'Please check username')
        return redirect("teacher_login")

class Change_password(View):
    def get(self, request):
        data = {'is_teacher':True}
        return render(request, "teachers/change_password.html", data)
    def post(self, request):
        old_pass = request.POST.get('old_pass')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            username = request.session.get('user')
            user = get_object_or_404(Teacher, username=username)
            flag = check_password(old_pass, user.password)
            if flag:
                user.password = make_password(pass1)
                user.save()
            else:
                messages.error(request, 'Please Check Your Password')
        else:
            messages.error(request, "New Password and Confirm Password Do not Match !")
        return redirect('teacher_change_password')




