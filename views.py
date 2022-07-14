from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
    
def contact(request):
    return render(request, 'pages/contact.html')

def _404(request):
    return render(request, 'pages/_404.html')

def _500(request):
    return render(request, 'pages/_500.html')