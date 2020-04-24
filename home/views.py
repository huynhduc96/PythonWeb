from django.shortcuts import render, redirect
from django.shortcuts import render

from django.views import View
from django.contrib.auth import authenticate, login, logout

from .form import RegisterForm
from .models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404


# Create your views here.
def index(request):
    data = {'Books': Book.objects.all()[:15], 'Books_Best': Book.objects.all()[:5]}
    return render(request, 'pages/index.html', data)


def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404("Not Exist")
    return render(request, 'pages/register.html', {'book': book})


class RegisterView(View):
    template_name = 'pages/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)

            return redirect('home')
        return render(request, self.template_name, {'errors': register_form.errors})
# Create your views here.
