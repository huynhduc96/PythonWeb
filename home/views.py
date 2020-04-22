from django.shortcuts import render
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {'Books': Book.objects.all()[:15], 'Books_Best': Book.objects.all()[:5]}
    return render(request, 'pages/index.html', data)
# Create your views here.
