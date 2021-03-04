from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from admins.models.notice import Notices
from admins.models.professor import Teacher, Role
from admins.models.leave import Leave
from datetime import date
from django.contrib import messages
from .index import validate_user




class Events(View):
    def get(self, request):
        validate_user(request)
        return render(request, 'teachers/events.html')


class All_notice(View):
    def get(self, request):
        validate_user(request)
        all_notice = Notices.objects.all().order_by('-date')
        data = {'all_notice' : all_notice}
        return render(request, 'teachers/notice.html', data)

class Apply_leave(View):
    def get(self, request):
        validate_user(request)
        return render(request, 'teachers/apply-leave.html')

    def post(self, request):
        data= request.POST
        validate_user(request)
        leave_type = data.get('leave-type')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        reason = data.get('reason')
        halfday = data.get('halfday', False)
        today = date.today()

        username = request.session.get('user')
        user = get_object_or_404(Teacher, username=username)
        leave = Leave(
            teacher = user,
            type = leave_type,
            start_date = start_date,
            reason = reason,
            is_teacher = True,
        )
        if halfday == True:
            leave.halfday = True
        if end_date != "":
            leave.end_date = end_date
        leave.save()

        return redirect('teacher_apply_leave')

class Students_leave(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Teacher, username=username)
        try:
            user_role = Role.objects.get(user = user.id)
        except:
            user_role = None
        if user_role is not None and user_role.role == "Class Teacher":
            leaves = Leave.objects.filter(is_student = True).order_by('-start_date')
            data = {'all_leaves':leaves, 'is_student':True}
            return render(request, 'teachers/view-leave.html', data)
        else:
            messages.error(request, 'You are not class teacher')
            return redirect('teacher_home')

class student_leave_status(View):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        status = kwargs.get('status')
        leave = get_object_or_404(Leave, pk=pk)
        leave.status=status
        leave.save()
        return redirect('teacher_students_leave')


class View_leave(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Teacher,username=username)
        leaves = Leave.objects.filter(teacher=user.pk).order_by('start_date')
        data = {'all_leaves': leaves,}
        return render(request, 'teachers/view-leave.html', data)



