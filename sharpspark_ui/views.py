# Create your views here.
from django.shortcuts import render

from forms import ContactForm

def index(request):
    context = {}
    return render(request, "sharpspark_ui/index.xhtml", context)

def about(request):
    context = {}
    return render(request, "sharpspark_ui/about.xhtml", context)

def contact(request):
    context = {'form' : ContactForm()}
    return render(request, "sharpspark_ui/contact.xhtml", context)

def enrol(request):
    context = {}
    return render(request, "sharpspark_ui/enrol.xhtml", context)

def blog(request):
    context = {}
    return render(request, "sharpspark_ui/blog.xhtml", context)
