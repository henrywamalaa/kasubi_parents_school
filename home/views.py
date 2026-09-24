from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    print("112")
    return render(request, 'about.html')

def academics(request):
    return render(request, 'academics.html')

def gallery(request):
    return render(request, 'gallery.html')

def news(request):
    return render(request, 'news.html')

def partnerships(request):
    return render(request, 'partnerships.html')

def contact(request):
    return render(request, 'contact.html')

def apply(request):
    return render(request, 'apply.html')