from django.shortcuts import render , redirect, get_object_or_404
from django.views import View
from admins.models.professor import Teacher
from admins.models.leave import Leave
from admins.models.notice import Notices

from .books import user_validate


class Index(View):
    def get(self, request):
        if user_validate(request):
            return render(request, 'library/index.html')
        else:
            return redirect('login')

class Apply_leave(View):
    def get(self, request):
        if user_validate(request):
            return render(request, 'library/apply-leave.html')
        else:
            return redirect('login')


    def post(self, request):
        if user_validate(request):
            data= request.POST

            leave_type = data.get('leave-type')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            reason = data.get('reason')
            halfday = data.get('halfday', False)
            # today = date.today()

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

            return redirect('library_apply_leave')
        else:
            return redirect('login')




class View_leave(View):
    def get(self, request):
        if user_validate(request):
            username = request.session.get('user')
            user = get_object_or_404(Teacher,username=username)
            leaves = Leave.objects.filter(teacher=user.pk).order_by('start_date')
            data = {'all_leaves': leaves,}
            return render(request, 'library/view-leave.html', data)
        else:
            return redirect('login')

class All_notice(View):
    def get(self, request):
        if user_validate(request):

            all_notice = Notices.objects.all().order_by('-date')
            data = {'all_notice' : all_notice}
            return render(request, 'library/notice.html', data)
        else:
            return redirect('login')




