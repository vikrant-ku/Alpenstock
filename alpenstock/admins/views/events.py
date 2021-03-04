from django.shortcuts import render , redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from admins.models.notice import Notices
from .login import validate_user

class Add_events(View):
    def get(self, request):
        if validate_user(request):
            return render(request, 'alpen_admin/events.html')
        return redirect('teacher_login')


class All_events(View):
    def get(self, request):
        if validate_user(request):
            return render(request, 'alpen_admin/events.html')
        return redirect('teacher_login')

class temp(View):
    def get(self,request):
        if validate_user(request):
            return render(request, 'alpen_admin/temp.html')
        return redirect('teacher_login')

class Add_notice(View):
    def get(self,request):
        if validate_user(request):
            return render(request, 'alpen_admin/add-notice.html')
        return redirect('teacher_login')


    def post(self, request):
        if validate_user(request):

            data = request.POST
            print(data)
            recipient = data.get('recipient')
            type = data.get('type')
            date = data.get('date')
            notice = data.get('notice')

            notic = Notices(
                recipient = recipient,
                type = type,
                date = date,
                notice = notice
                )
            notic.save()
            return redirect('add_notice')
        return redirect('teacher_login')

class All_notice(View):
    def get(self, request):
        if validate_user(request):
            q = request.GET.get('q')
            if q is not None:
                notices = Notices.objects.filter(
                                        Q(recipient__icontains=q)
                                        | Q(type__icontains=q)
                                        | Q(date__icontains=q)
                                        | Q(notice__icontains=q)
                                         ).order_by('-date')

                if len(notices)>0:
                    all_notice = notices
                else:
                    all_notice = Notices.objects.all().order_by('-date')
            else:
                all_notice = Notices.objects.all().order_by('-date')

            data = {'all_notice':all_notice, "is_admin":True}
            return render(request,'alpen_admin/notice.html', data )
        return redirect('teacher_login')

class Delete_notice(View):
    def get(self, request, **kwargs):
        if validate_user(request):
            id = kwargs.get('pk')
            notic = get_object_or_404(Notices, pk=id)
            notic.delete()
            return redirect('admin_notice')
        return redirect('teacher_login')




