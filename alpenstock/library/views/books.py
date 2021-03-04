from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from library.models import Books
from django.contrib import messages
from admins.models.professor import Teacher, Role
from admins.models.students import Students
from library.models import Issue_book


class Index(View):
    def get(self, request):
        if user_validate(request):
            return render(request, 'library/index.html')
        else:
            return redirect('login')



class Add_books(View):
    def get(self, request):
        if user_validate(request):
            return render(request, 'library/add-books.html')
        else:
            return redirect('login')

    def post(self, request):
        data = request.POST
        book_name = data.get("book_name")
        author_name = data.get("author_name")
        publish_year = data.get("publish_year")
        isbn_num = data.get("isbn_num")
        publication = data.get("publication")
        edition = data.get("edition")
        no_of_copies = data.get("no_of_copies")
        price = data.get("price")
        cupbord = data.get("cupbord")
        rack = data.get("rack")

        try:
            book = Books.objects.get(isbn_number = str(isbn_num))
            messages.error(request, 'Please Check book ISBN number')
        except:
            book = Books(
                book_name = book_name,
                auther_name = author_name,
                publishing_year = publish_year,
                isbn_number = isbn_num,
                publication = publication,
                edition = edition,
                number_of_copies = no_of_copies,
                price = price,
                cupbord_number = cupbord,
                rack_number = rack

            )
            book.save()
        return redirect('add_books')

class All_books(View):
    def get(self, request):
        if user_validate(request):
            books = Books.objects.all()
            data = {'books': books}
            return render(request, 'library/all-books.html', data)
        else:
            return redirect('login')


class Delete_book(View):
    def get(self, request, **kwargs):
        if user_validate(request):
            id = kwargs.get('pk')
            book = get_object_or_404(Books, pk=id)
            book.delete()
            messages.success(request, f"{book.book_name} successfully deleted")
            return redirect('all_books')
        else:
            return redirect('login')


class Edit_book(View):
    def get(self, request, **kwargs):
        if user_validate(request):
            id = kwargs.get('pk')
            book = get_object_or_404(Books, pk=id)
            data = {'book':book}
            return render(request, 'library/edit-book.html', data)
        else:
            return redirect('login')

    def post(self, request, **kwargs):
        return_url= request.META['PATH_INFO']
        id = kwargs.get('pk')
        data = request.POST

        book_name = data.get("book_name")
        author_name = data.get("author_name")
        publish_year = data.get("publish_year")
        isbn_num = data.get("isbn_num")
        publication = data.get("publication")
        edition = data.get("edition")
        no_of_copies = data.get("no_of_copies")
        price = data.get("price")
        cupbord = data.get("cupbord")
        rack = data.get("rack")


        book = Books.objects.get(isbn_number = str(isbn_num))
        if book.id == id:

            book.book_name = book_name
            book.auther_name = author_name
            book.publishing_year = publish_year
            book.isbn_number = isbn_num
            book.publication = publication
            book.edition = edition
            book.number_of_copies = no_of_copies
            book.price = price
            book.cupbord_number = cupbord
            book.rack_number = rack

            book.save()
        else:
            messages.error(request, f"{isbn_num} is Available please Confirm ISBN Number.")
        return HttpResponseRedirect(return_url)

class Issue_books(View):
    def get(self, request):
        if user_validate(request):
            return render(request, 'library/issue-book.html')
        else:
            return redirect('login')

    def post(self, request):
        data = request.POST
        return_date = data.get('return_date')
        username = data.get('username')

        book_name = data.get('book_name')
        book_dict = book_name.split(",")
        book = Books.objects.get(book_name=book_dict[0], edition=book_dict[1].strip())
        issue_book = Issue_book(
            book = book,
            return_date = return_date,
        )
        if "ST" in username:
            user = get_object_or_404(Students, username=username)
            issue_book.student = user
        else:
            user = get_object_or_404(Teacher, username=username)
            issue_book.teacher = user

        issue_book.save()
        messages.success(request, f"{book_dict[0]} is issued to {username}")
        return redirect("issue_book")

class All_issue_book(View):
    def get(self, request):
        if user_validate(request):
            all_issues = Issue_book.objects.all()

            data = {'all_issue_book':all_issues}
            return render(request, 'library/all-issue-book.html', data)
        else:
            return redirect('login')

def search_user(request):
    if user_validate(request):
        data = {}
        username = False
        user = request.GET.get('user')
        if 'ST' in user:
            try:
                username = Students.objects.get(username = user)
            except:
                messages.error(request,'Please check userID')
        elif 'TE' in user:
            try:
                username = Teacher.objects.get(username = user)
            except:
                messages.error(request, 'Please check userID')
        else:
            messages.error(request, 'Please check userID')

        if username:
            books = Books.objects.all()
            data = {'user' : username, 'books':books}

        return render(request, 'library/issue-book.html', data)
    else:
        return redirect('login')


def user_validate(request):
    username = request.session.get('user')
    user = get_object_or_404(Teacher, username= username)
    role = get_object_or_404(Role, user = user)
    if role.role == "Librarian":
        return True
    else:
        return False






