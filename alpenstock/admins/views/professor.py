from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View
from admins.models.professor import Teacher, Role
from admins.models.leave import Leave
from admins.models.classes import Class
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from .student import proper_pagination
from .login import validate_user



class Add_professors(View):
    def get(self, request):
        if validate_user(request):
            return render(request, 'alpen_admin/add-professor.html')
        return redirect('teacher_login')

    def post(self, request):
        if validate_user(request):
            data = request.POST
            try:
                image = request.FILES['image']
            except:
                image = None

            firstname = data.get('firstname')
            lastname = data.get('lastname')
            gender = data.get('gender')
            dob = data.get('dob')
            address = data.get('address')
            country = data.get('country')
            state = data.get('state')
            city = data.get('city')
            postcode = data.get('postcode')
            mobileno = data.get('mobileno')
            email = data.get('email')
            pass1 = data.get('pass1')
            pass2 = data.get('pass2')

            designation = data.get('designation')
            qualification = data.get('qualification')
            salary = data.get('salary')
            contract = data.get('contract')
            shift = data.get('shift')
            bank = data.get('bank')
            branch = data.get('branch')
            account = data.get('account')
            ifsc = data.get('ifsc')
            pan = data.get('pan')
            aadhar = data.get('aadhar')
            description = data.get('description')

            if pass1==pass2 and gender is not None:

                user = Teacher(
                    first_name = firstname,
                    last_name = lastname,
                    gender = gender,
                    dob = dob,
                    address = address,
                    country = country,
                    state = state,
                    city = city,
                    zipcode = postcode,
                    phone = mobileno,
                    email = email,
                    designation = designation,
                    qualification = qualification,
                    basic_salary = salary,
                    contract_type = contract,
                    work_shift = shift,
                    # account info
                    bank_name = bank,
                    branch_name = branch,
                    account_number = account,
                    ifsc_code = ifsc,
                    aadhar_number =aadhar,
                    pancard_number = pan,
                    descripation =description,

                    )
                user.password = make_password(pass1)
                user.save()
                user.username = "TE00"+str(user.id)

                if image is not None:
                    user.image= image
                user.save()

            elif gender is None:
                messages.error(request, "Please select Gender")
            else:
                messages.error(request,"password do not match")
            return redirect('add_teacher')
        return redirect('teacher_login')

class All_professor(View):

    def get(self, request):
        if validate_user(request):

            all_teacher = Teacher.objects.all()

            # paginator
            paginator = Paginator(all_teacher, 1)
            page = request.GET.get('page')

            try:
                allteacher = paginator.page(page)
            except PageNotAnInteger:
                allteacher = paginator.page(1)
            except EmptyPage:
                allteacher = paginator.page(paginator.num_pages)

            if page is None:
                start_index = 0
                end_index = 7
            else:
                (start_index, end_index) = proper_pagination(allteacher, index=1)

            page_range = list(paginator.page_range)[start_index:end_index]

            if page is None or page == 1:
                count = 1
            else:
                count = allteacher.start_index()


            data = {'all_teacher': allteacher, 'page_range': page_range, 'count': count}
            return render(request, 'alpen_admin/all-professors.html', data)
        return redirect('teacher_login')


class Edit_professor(View):
    def get(self, request, **kwargs):
        if validate_user(request):
            id = kwargs.get('pk')
            user = Teacher.objects.get(pk=id)
            data = {'teacher':user}
            return render(request, 'alpen_admin/edit-professor.html', data )
        return redirect('login')

    def post(self, request, **kwargs):
        path = request.META['PATH_INFO']
        data = request.POST
        try:
            image = request.FILES['image']
        except:
            image = None

        id = kwargs.get('pk')
        try:
            user = Teacher.objects.get(pk=id)
        except:
            user = None

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        gender = data.get('gender')
        dob = data.get('dob')
        address = data.get('address')
        country = data.get('country')
        state = data.get('state')
        city = data.get('city')
        postcode = data.get('postcode')
        mobileno = data.get('mobileno')
        email = data.get('email')
        designation = data.get('designation')
        qualification = data.get('qualification')
        salary = data.get('salary')
        contract = data.get('contract')
        shift = data.get('shift')
        bank = data.get('bank')
        branch = data.get('branch')
        account = data.get('account')
        ifsc = data.get('ifsc')
        pan = data.get('pan')
        aadhar = data.get('aadhar')
        description = data.get('description')

        if user is not None:
            user.first_name = firstname
            user.last_name = lastname
            user.dob = dob
            user.address = address
            user.country = country
            user.state = state
            user.city = city
            user.zipcode = postcode
            user.phone = mobileno
            user.email = email
            user.designation = designation
            user.qualification = qualification
            user.basic_salary = salary
            user.contract_type = contract
            user.work_shift = shift
                    # account info
            user.bank_name = bank
            user.branch_name = branch
            user.account_number = account
            user.ifsc_code = ifsc
            user.aadhar_number = aadhar
            user.pancard_number = pan
            user.descripation = description

            if gender is not None:
                user.gender = gender
            if image is not None:
                user.image = image
            user.save()

        return HttpResponseRedirect(path)


class Delete_professor(View):
    def get(self, request,*arge, **kwargs):
        if validate_user(request):
            id = kwargs.get('pk')
            user = get_object_or_404(Teacher, pk=id)
            user.delete()
            return redirect("all_teachers")
        return redirect('login')

class Assign_role(View):
    def get(self, request, **kwargs):
        if validate_user(request):
            id = kwargs.get('pk')
            user = Teacher.objects.get(pk=id)
            cls = Class.objects.all()
            data = {"classes":cls, 'teacher':user}
            return render(request, 'alpen_admin/assign-role.html', data)
        return redirect('login')

    def post(self,request, **kwargs):
        if validate_user(request):
            returnUrl = request.META['PATH_INFO']
            data = request.POST
            user = data.get('username')
            role = data.get('role')
            class_name = data.get('class')
            section = data.get('section')
            username = get_object_or_404(Teacher, username= user)

            role = Role(user=username, role=role)
            if class_name is not None:
                cls = get_object_or_404(Class, class_name=class_name)
                role.class_name=cls
                role.section=section

            role.save()
            return HttpResponseRedirect(returnUrl)
        return redirect('login')

class teacher_leave(View):
    def get(self, request):
        if validate_user(request):
            leaves = Leave.objects.filter(is_teacher = True).order_by('-start_date')
            data = {'all_leaves':leaves}
            return render(request, 'alpen_admin/view-leave.html', data)
        return redirect('login')




class teacher_leave_status(View):
    def get(self, request, **kwargs):
        if validate_user(request):
            pk = kwargs.get('pk')
            status = kwargs.get('status')
            leave = get_object_or_404(Leave, pk=pk)
            leave.status=status
            leave.save()
            return redirect('teachers_leave')
        return redirect('login')
