from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from admins.models.notice import Notices
from admins.models.leave import Leave
from admins.models.students import Students
from .index import validate_user

class Events(View):
    def get(self, request):
        validate_user(request)
        return render(request, 'students/events.html')

class All_notice(View):
    def get(self, request):
        validate_user(request)
        all_notice = Notices.objects.filter(recipient='Students')

        data = {'all_notice' : all_notice}
        return render(request, 'students/notice.html', data)

class Apply_leave(View):
    def get(self, request):
        validate_user(request)
        return render(request, 'students/apply-leave.html')

    def post(self, request):
        data= request.POST
        validate_user(request)
        leave_type = data.get('leave-type')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        reason = data.get('reason')
        halfday = data.get('halfday', False)
        username = request.session.get('user')
        user = get_object_or_404(Students, username=username)
        leave = Leave(
            student= user,
            type = leave_type,
            start_date = start_date,
            reason = reason,
            is_student = True,
        )
        if halfday:
            leave.halfday = True
        if end_date != "":
            leave.end_date = end_date
        leave.save()

        return redirect('apply_leave')

class All_leaves(View):
    def get(self, request):
        validate_user(request)
        username = request.session.get('user')
        user = get_object_or_404(Students, username=username)
        leaves = Leave.objects.filter(student=user.id)
        data = {'all_leaves' :leaves}
        return render(request, 'students/view-leave.html', data)