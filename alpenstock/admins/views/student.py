from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View
from admins.models.students import Students
from admins.models.classes import Class
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from .login import validate_user

class Add_students(View):
    def get(self, request):
        if validate_user(request):
            classes = Class.objects.all()
            data = {'classes': classes}
            return render(request, 'alpen_admin/add-student.html', data)
        return redirect('login')

    def post(self, request):
        if validate_user(request):
            data = request.POST
            try:
                image = request.FILES['image']
            except:
                image = None
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            fathername = data.get('fathername')
            mothername = data.get('mothername')
            admission_no = str(data.get('admno'))
            address = data.get('address')
            country = data.get('country')
            state = data.get('state')
            city = data.get('city')
            postcode = data.get('postcode')
            image = data.get('image')
            phone = data.get('mobileno')
            dob = data.get('dob')
            class_name = data.get('class')
            section = data.get('section')
            gender = data.get('gender')
            pass1= data.get('pass1')
            pass2= data.get('pass2')
            if pass1==pass2:

                try:
                    class_name = Class.objects.get(class_name=class_name)
                except:
                    messages.error(request, 'Class name is not valid or exist')
                    return redirect('add_students')
                try:
                    user = Students.objects.get(admission_no = admission_no)
                    messages.error(request, 'This Admission number is Available Please Confirm admission number !!')
                    return redirect('add_students')
                except:
                    pass

                user = Students(

                    password = pass1,
                    admission_no = admission_no,
                    first_name = firstname,
                    last_name = lastname,
                    father_name = fathername,
                    mother_name = mothername,
                    dob = dob,
                    address = address,
                    country = country,
                    state = state,
                    city = city,
                    zipcode = postcode,
                    phone = phone,
                    gender = gender,
                    class_name = class_name,
                    section = section
                        )
                user.password = make_password(user.password)
                user.save()
                user.username = "ST00"+str(user.id)

                if image is not None:
                    user.image = image
                user.save()
                messages.success(request, f'{user.username} is registered')
            else:
                messages.error(request, 'password do not registered')
            return redirect('add_students')
        return redirect('login')

class All_students(View):

    def get(self, request):
        if validate_user(request):
            all_stud = Students.objects.all()
            #paginator
            paginator = Paginator(all_stud, 1)
            page = request.GET.get('page')


            try:
                allstud = paginator.page(page)
            except PageNotAnInteger:
                allstud = paginator.page(1)
            except EmptyPage:
                allstud = paginator.page(paginator.num_pages)

            if page is None:
                start_index = 0
                end_index= 7
            else:
                (start_index, end_index)=proper_pagination(allstud, index=1)

            page_range = list(paginator.page_range)[start_index:end_index]

            if page is None or page==1:
                count = 1
            else:
                count = allstud.start_index()
                print(count)

            data = {'all_stud': allstud, 'page_range': page_range, 'count': count}
            return render(request, 'alpen_admin/all-students.html', data)
        return redirect('login')


class Edit_student(View):
    def get(self, request, **kwargs):
        if validate_user(request):
            id = kwargs.get('pk')
            user = Students.objects.get(pk=id)
            classes = Class.objects.all()
            data = {'student':user , 'classes': classes }
            return render(request, 'alpen_admin/edit-student.html', data )
        return redirect('login')

    def post(self, request, **kwargs):
        if validate_user(request):
            path = request.META['PATH_INFO']
            id = kwargs.get('pk')
            try:
                image = request.FILES['image']
            except:
                image = None
            user = Students.objects.get(pk=id)

            data = request.POST
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            fathername = data.get('fathername')
            mothername = data.get('mothername')
            admission_no = data.get('admno')
            address = data.get('address')
            country = data.get('country')
            state = data.get('state')
            city = data.get('city')
            postcode = data.get('postcode')
            image = data.get('image')
            phone = data.get('mobileno')
            dob = data.get('dob')
            class_name = data.get('class')
            section = data.get('section')
            gender = data.get('gender')

            if class_name is not None:
                try:
                    class_name = Class.objects.get(class_name=class_name)
                except:
                    messages.error(request, 'Class name is not valid or exist')
                    return HttpResponseRedirect(path)

            user.admission_no = admission_no
            user.first_name = firstname
            user.last_name = lastname
            user.father_name = fathername
            user.mother_name = mothername
            user.dob = dob
            user.address = address
            user.country = country
            user.state = state

            user.city = city
            user.zipcode = postcode
            user.phone = phone
            if gender is not None:
                user.gender = gender
            if class_name is not None:
                user.class_name = class_name
            if section is not None:
                user.section = section
            if image is not None:
                user.image = image

            user.save()

            return HttpResponseRedirect(path)
        return redirect('login')

class Delete_student(View):
    def get(self, request,*arge, **kwargs):
        if validate_user(request):

            pk = kwargs.get('pk')
            stud = get_object_or_404(Students, pk=pk)
            stud.delete()
            return redirect("all_students")
        return redirect('login')


def proper_pagination(prods, index):
    start_index = 0
    end_index = 7
    if prods.number > index:
        start_index = prods.number - index
        end_index = start_index + end_index
    return (start_index,end_index)